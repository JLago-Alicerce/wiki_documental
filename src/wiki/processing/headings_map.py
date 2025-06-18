from __future__ import annotations

import re
from pathlib import Path
from typing import List, Dict

import yaml
from wiki.config import cfg
from wiki.utils.slug import safe_slug

used_slugs: set[str] = set()

NUMBER_RE = re.compile(r"^\d+(\.\d+)*\s+")


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def build_headings_map(
    md_folder: Path,
    *,
    strip_numbers: bool = True,
    from_level: int = 1,
) -> List[Dict[str, str | int]]:
    """Return a list of heading data dictionaries."""
    map_data: List[Dict[str, str | int]] = []
    used_slugs.clear()
    counters: dict[int, int] = {}

    styles_cfg = cfg.get("headings", {}).get("styles")
    patterns: list[tuple[re.Pattern[str], int]] | None = None
    if styles_cfg:
        patterns = [
            (re.compile(rf"^{re.escape(s)}\s+(.*)$"), int(level))
            for s, level in sorted(styles_cfg.items(), key=lambda x: -len(x[0]))
        ]

    for md_file in sorted(md_folder.rglob("*.md")):
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if patterns:
                    match = None
                    level = 0
                    title = ""
                    for pat, lvl in patterns:
                        m = pat.match(stripped)
                        if m:
                            match = m
                            level = lvl
                            title = m.group(1).strip()
                            break
                    if not match:
                        continue
                else:
                    m = HEADING_RE.match(stripped)
                    if not m:
                        continue
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

                    filename = f"{slug}.md"

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
            filename = f"{slug}.md"

        enriched.append({"id": identifier, **item, "filename": filename})

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(enriched, f, allow_unicode=True)
