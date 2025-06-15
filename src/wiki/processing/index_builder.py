from __future__ import annotations

from typing import List, Dict, Any
import re

MAX_LEVEL = 2


def build_index_from_map(map_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Generate hierarchical index data from headings map."""
    index: List[Dict[str, Any]] = []
    stack: List[tuple[int, Dict[str, Any]]] = []
    counters: dict[int, int] = {}

    for item in map_data:
        level = int(item.get("level", 1))
        if level > MAX_LEVEL:
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
        entry = {
            "id": ".".join(id_parts),
            "title": item.get("title"),
            "slug": item.get("slug"),
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
