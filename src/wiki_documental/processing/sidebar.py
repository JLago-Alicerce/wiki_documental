from __future__ import annotations

from pathlib import Path
from typing import List, Dict

import yaml


def build_sidebar(index_path: Path, output_path: Path) -> None:
    """Crea _sidebar.md jerárquico a partir de index.yaml."""

    with index_path.open("r", encoding="utf-8") as f:
        index_data: List[Dict[str, object]] = yaml.safe_load(f) or []

    lines: List[str] = ["* [Inicio](README.md)\n"]

    def add_entries(entries: List[Dict[str, object]], level: int) -> None:
        indent = "  " * level
        for entry in entries:
            slug = entry.get("slug")
            title = entry.get("title")
            identifier = str(entry.get("id", "")).replace(".", "-")
            file_name = f"{identifier}_{slug}.md"
            lines.append(f"{indent}* [{title}]({file_name})\n")
            children = entry.get("children") or []
            add_entries(children, level + 1)

    add_entries(index_data, 0)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)
