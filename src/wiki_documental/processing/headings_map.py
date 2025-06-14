from __future__ import annotations

import re
from pathlib import Path
from typing import List, Dict

import yaml
from ..utils import safe_slug

NUMBER_RE = re.compile(r"^\d+(\.\d+)*\s+")


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def build_headings_map(
    md_folder: Path,
    *,
    strip_numbers: bool = True,
    from_level: int = 2,
) -> List[Dict[str, str | int]]:
    """Return a list of heading data dictionaries."""
    map_data: List[Dict[str, str | int]] = []
    used_slugs: set[str] = set()
    for md_file in md_folder.rglob("*.md"):
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                m = HEADING_RE.match(line.strip())
                if m:
                    level = len(m.group(1))
                    title = m.group(2).strip()
                    if strip_numbers and level >= from_level:
                        title = NUMBER_RE.sub("", title)
                    slug = safe_slug(title, used_slugs, max_len=60)
                    used_slugs.add(slug)
                    map_data.append(
                        {
                            "level": level,
                            "title": title,
                            "slug": slug,
                        }
                    )
    return map_data


def save_map_yaml(map_data: List[Dict[str, str | int]], path: Path) -> None:
    """Save map data to YAML file with id/slug pairs."""
    counters: dict[int, int] = {}
    enriched: List[Dict[str, str | int]] = []
    for item in map_data:
        level = int(item.get("level", 1))
        counters[level] = counters.get(level, 0) + 1
        for l in list(counters.keys()):
            if l > level:
                del counters[l]
        id_parts = [str(counters[i]) for i in range(1, level + 1) if i in counters]
        enriched.append({"id": ".".join(id_parts), **item})

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(enriched, f, allow_unicode=True)
