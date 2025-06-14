from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any

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
    for item in data:
        slug = item.get("slug")
        if slug and _slug_level(slug) <= 2:
            slugs.add(slug)
    return slugs


def _extract_slugs(entries: List[Dict[str, Any]]) -> set[str]:
    slugs: set[str] = set()
    for entry in entries:
        slug = entry.get("slug")
        if slug and _slug_level(slug) <= 2:
            slugs.add(slug)
        children = entry.get("children", [])
        if children:
            slugs.update(_extract_slugs(children))
    return slugs


def _load_index_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return _extract_slugs(data)


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
