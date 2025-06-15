from __future__ import annotations

from pathlib import Path
from typing import List, Dict

import yaml


def build_sidebar(index_path: Path, output_path: Path, depth: int = 1) -> None:
    """Crea _sidebar.md jerárquico a partir de index.yaml.

    Parameters
    ----------
    index_path : Path
        Ruta al archivo ``index.yaml``.
    output_path : Path
        Ruta del ``_sidebar.md`` a generar.
    depth : int, optional
        Profundidad máxima de títulos a incluir. ``1`` solo agrega los
        encabezados de primer nivel.
    """

    with index_path.open("r", encoding="utf-8") as f:
        index_data: List[Dict[str, object]] = yaml.safe_load(f) or []

    lines: List[str] = []
    readme = output_path.parent / "README.md"
    if readme.exists():
        lines.append("* [Inicio](README.md)\n")

    def add_entries(entries: List[Dict[str, object]], level: int) -> None:
        indent = "  " * level
        for entry in entries:
            slug = entry.get("slug")
            title = entry.get("title")
            identifier = str(entry.get("id", ""))
            parts = identifier.split(".")
            doc_id = parts[0]
            section_id = "-".join(parts[1:])
            prefix = f"{doc_id}_{section_id}" if section_id else doc_id
            file_name = f"{prefix}_{slug}.md"
            lines.append(f"{indent}* [{title}]({file_name})\n")
            children = entry.get("children") or []
            if level + 1 < depth:
                add_entries(children, level + 1)

    add_entries(index_data, 0)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)
