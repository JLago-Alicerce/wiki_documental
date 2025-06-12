from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any

import yaml


def _load_map_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return {item.get("slug") for item in data if item.get("slug")}


def _extract_slugs(entries: List[Dict[str, Any]]) -> set[str]:
    slugs: set[str] = set()
    for entry in entries:
        slug = entry.get("slug")
        if slug:
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
