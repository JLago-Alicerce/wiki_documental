from __future__ import annotations

from typing import List, Dict, Any
import re

from wiki.config import cfg
from wiki.utils.slug import slug_to_label


def build_index_from_map(
    map_data: List[Dict[str, Any]],
    max_depth: int | None = None,
) -> List[Dict[str, Any]]:
    """Generate hierarchical index data from headings map."""
    if max_depth is None:
        max_depth = int(cfg.get("menu", {}).get("depth_limit", 2))
    index: List[Dict[str, Any]] = []
    stack: List[tuple[int, Dict[str, Any]]] = []
    counters: dict[int, int] = {}

    for item in map_data:
        level = int(item.get("level", 1))
        if level > max_depth:
            continue
        title = str(item.get("title", ""))
        title_clean = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", title)
        title_clean = re.sub(r"<img[^>]*>", "", title_clean, flags=re.I)
        if not title_clean.strip():
            continue
        counters[level] = counters.get(level, 0) + 1
        for l in list(counters.keys()):
            if l > level:
                del counters[l]
        id_parts = [str(counters[i]) for i in range(1, level + 1) if i in counters]
        slug = item.get("slug")
        entry = {
            "id": ".".join(id_parts),
            "title": item.get("title"),
            "slug": slug,
            "label": slug_to_label(str(slug)) if slug else None,
            "visible": True,
            "children": [],
        }
        while stack and stack[-1][0] >= level:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(entry)
        else:
            index.append(entry)
        stack.append((level, entry))

    return index
