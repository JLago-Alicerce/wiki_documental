from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any
import re

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


def existing_md_slugs(docs_dir: Path) -> set[str]:
    """Return slugs of Markdown files within ``docs_dir``."""
    slugs: set[str] = set()
    for md in docs_dir.rglob("*.md"):
        if md.name == "_sidebar.md":
            continue
        slugs.add(md.stem)
    return slugs


def extract_sidebar_slugs(sidebar_path: Path) -> set[str]:
    """Devuelve todos los slugs presentes en el _sidebar.md, manejando niveles anidados."""
    if not sidebar_path.exists():
        return set()
    slugs: set[str] = set()
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for line in sidebar_path.read_text(encoding="utf-8").splitlines():
        m = pattern.search(line)
        if m:
            slug = Path(m.group(1)).stem
            slugs.add(slug)
    return slugs


def compare_index_docs(index_path: Path, docs_dir: Path) -> Dict[str, List[str]]:
    """Compare index slugs with markdown files."""
    index_slugs = _load_index_slugs(index_path)
    md_slugs = existing_md_slugs(docs_dir)
    return {
        "docs_not_in_index": sorted(md_slugs - index_slugs),
        "index_missing_docs": sorted(index_slugs - md_slugs),
    }


def compare_sidebar_docs(sidebar_path: Path, docs_dir: Path) -> Dict[str, List[str]]:
    """Return sidebar links pointing to missing documents."""
    sidebar_slugs = extract_sidebar_slugs(sidebar_path)
    md_slugs = existing_md_slugs(docs_dir)
    return {"broken_sidebar_links": sorted(sidebar_slugs - md_slugs)}


def verify_pre_ingest(
    map_path: Path,
    index_path: Path,
    *,
    strict: bool = True,
    docs_dir: Path | None = None,
    sidebar_path: Path | None = None,
) -> bool:
    """Verify map, index and sidebar coherence."""

    diffs = compare_map_index(map_path, index_path)
    docs_diffs = {"docs_not_in_index": [], "index_missing_docs": []}
    sidebar_diffs = {"broken_sidebar_links": []}
    if docs_dir is not None and docs_dir.exists():
        docs_diffs = compare_index_docs(index_path, docs_dir)
        if sidebar_path is not None and sidebar_path.exists():
            sidebar_diffs = compare_sidebar_docs(sidebar_path, docs_dir)

    ok = (
        not diffs["missing_in_index"]
        and not diffs["missing_in_map"]
        and not docs_diffs["docs_not_in_index"]
        and not docs_diffs["index_missing_docs"]
        and not sidebar_diffs["broken_sidebar_links"]
    )
    if ok:
        return True

    table = Table(title="Differences")
    table.add_column("Type")
    table.add_column("Slugs")
    table.add_row("Missing in index", ", ".join(diffs["missing_in_index"]) or "-")
    table.add_row("Missing in map", ", ".join(diffs["missing_in_map"]) or "-")
    if docs_dir is not None:
        table.add_row(
            "Docs not in index",
            ", ".join(docs_diffs["docs_not_in_index"]) or "-",
        )
        table.add_row(
            "Index missing docs",
            ", ".join(docs_diffs["index_missing_docs"]) or "-",
        )
    if sidebar_path is not None:
        table.add_row(
            "Sidebar broken",
            ", ".join(sidebar_diffs["broken_sidebar_links"]) or "-",
        )

    console = Console()
    if strict:
        console.print(table)
        return False

    console.print(table, style="yellow")
    return True
