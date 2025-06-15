from __future__ import annotations

import re
from pathlib import Path
from typing import List, Dict

import yaml
from wiki.utils.slug import safe_slug

used_slugs: set[str] = set()

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
    used_slugs.clear()
    counters: dict[int, int] = {}
    for md_file in sorted(md_folder.rglob("*.md")):
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                m = HEADING_RE.match(line.strip())
                if m:
                    level = len(m.group(1))
                    title = m.group(2).strip()
                    if strip_numbers and level >= from_level:
                        title = NUMBER_RE.sub("", title)

                    counters[level] = counters.get(level, 0) + 1
                    for l in list(counters.keys()):
                        if l > level:
                            del counters[l]
                    id_parts = [str(counters[i]) for i in range(1, level + 1) if i in counters]
                    identifier = ".".join(id_parts)

                    slug = safe_slug(title, used_slugs)

                    parts = identifier.split(".")
                    doc_id = parts[0]
                    section_id = "-".join(parts[1:])
                    prefix = f"{doc_id}_{section_id}" if section_id else doc_id
                    filename = f"{prefix}_{slug}.md"

                    map_data.append(
                        {
                            "id": identifier,
                            "level": level,
                            "title": title,
                            "slug": slug,
                            "filename": filename,
                        }
                    )
    return map_data


def save_map_yaml(map_data: List[Dict[str, str | int]], path: Path) -> None:
    """Save map data to YAML file."""
    counters: dict[int, int] = {}
    enriched: List[Dict[str, str | int]] = []
    for item in map_data:
        level = int(item.get("level", 1))
        identifier = item.get("id")
        if identifier is None:
            counters[level] = counters.get(level, 0) + 1
            for l in list(counters.keys()):
                if l > level:
                    del counters[l]
            id_parts = [str(counters[i]) for i in range(1, level + 1) if i in counters]
            identifier = ".".join(id_parts)

        slug = str(item.get("slug", ""))
        filename = item.get("filename")
        if not filename and identifier and slug:
            parts = str(identifier).split(".")
            doc_id = parts[0]
            section_id = "-".join(parts[1:])
            prefix = f"{doc_id}_{section_id}" if section_id else doc_id
            filename = f"{prefix}_{slug}.md"

        enriched.append({"id": identifier, **item, "filename": filename})

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(enriched, f, allow_unicode=True)
