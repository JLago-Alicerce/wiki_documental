from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any

from rich.console import Console
from rich.table import Table

import yaml
from .index_builder import build_index_from_map


def _slug_level(slug: str) -> int:
    """Return heading level from slug based on hyphen count."""
    return slug.count("-") + 1


def _load_map_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    slugs: set[str] = set()
    for idx, item in enumerate(data):
        slug = item.get("slug")
        level = int(item.get("level", 1))
        if not slug or level > 2:
            continue
        if level == 2:
            has_child = False
            for nxt in data[idx + 1 :]:
                nxt_level = int(nxt.get("level", 1))
                if nxt_level <= level:
                    break
                if nxt_level > level:
                    has_child = True
                    break
            if not has_child:
                continue
        slugs.add(slug)
    return slugs


def _extract_slugs(entries: List[Dict[str, Any]], *, level: int = 1) -> set[str]:
    slugs: set[str] = set()
    for entry in entries:
        slug = entry.get("slug")
        children = entry.get("children", [])
        if slug and level <= 2:
            if not (level == 2 and not children):
                slugs.add(slug)
        if children:
            slugs.update(_extract_slugs(children, level=level + 1))
    return slugs


def _load_index_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return _extract_slugs(data, level=1)


def compare_map_index(map_path: Path, index_path: Path) -> Dict[str, List[str]]:
    """Return differences between map and index slugs."""
    map_slugs = _load_map_slugs(map_path)
    index_slugs = _load_index_slugs(index_path)
    return {
        "missing_in_index": sorted(map_slugs - index_slugs),
        "missing_in_map": sorted(index_slugs - map_slugs),
    }


def repair_index(map_path: Path, index_path: Path) -> None:
    """Rebuild index.yaml from map.yaml."""
    if not map_path.exists():
        return
    with map_path.open("r", encoding="utf-8") as f:
        map_data: List[Dict[str, Any]] = yaml.safe_load(f) or []
    index_data = build_index_from_map(map_data)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(index_data, f, allow_unicode=True)


def verify_pre_ingest(map_path: Path, index_path: Path, *, strict: bool = True) -> bool:
    """Verify map and index coherence.

    If ``strict`` is ``False`` the differences are displayed as warnings and
    ``True`` is returned regardless of mismatches.
    """
    diffs = compare_map_index(map_path, index_path)
    if not diffs["missing_in_index"] and not diffs["missing_in_map"]:
        return True

    table = Table(title="Differences")
    table.add_column("Type")
    table.add_column("Slugs")
    table.add_row("Missing in index", ", ".join(diffs["missing_in_index"]) or "-")
    table.add_row("Missing in map", ", ".join(diffs["missing_in_map"]) or "-")

    console = Console()
    if strict:
        console.print(table)
        return False

    console.print(table, style="yellow")
    return True
