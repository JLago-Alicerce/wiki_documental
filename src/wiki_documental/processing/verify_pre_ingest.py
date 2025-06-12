from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import yaml


def _load_map_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return {item.get("slug") for item in data if item.get("slug")}


def _load_index_slugs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    slugs: set[str] = set()
    for entry in data:
        slug = entry.get("slug")
        if slug:
            slugs.add(slug)
        for child in entry.get("children", []):
            child_slug = child.get("slug")
            if child_slug:
                slugs.add(child_slug)
    return slugs


def compare_map_index(map_path: Path, index_path: Path) -> Dict[str, List[str]]:
    """Return differences between map and index slugs."""
    map_slugs = _load_map_slugs(map_path)
    index_slugs = _load_index_slugs(index_path)
    return {
        "missing_in_index": sorted(map_slugs - index_slugs),
        "missing_in_map": sorted(index_slugs - map_slugs),
    }
