from __future__ import annotations

import re
from pathlib import Path
from typing import List, Dict

import yaml
from slugify import slugify


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def build_headings_map(md_folder: Path) -> List[Dict[str, str | int]]:
    """Devuelve lista de dicts: [{'level': 1, 'title': '...', 'slug': '...'}, ...]"""
    map_data: List[Dict[str, str | int]] = []
    for md_file in md_folder.rglob("*.md"):
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                m = HEADING_RE.match(line.strip())
                if m:
                    level = len(m.group(1))
                    title = m.group(2).strip()
                    map_data.append(
                        {
                            "level": level,
                            "title": title,
                            "slug": slugify(title),
                        }
                    )
    return map_data


def save_map_yaml(map_data: List[Dict[str, str | int]], path: Path) -> None:
    """Save map data to YAML file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(map_data, f, allow_unicode=True)
