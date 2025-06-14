from __future__ import annotations

from pathlib import Path
from typing import List, Dict

import yaml


def build_sidebar(map_path: Path, output_path: Path, depth: int = 1) -> None:
    """Generate ``_sidebar.md`` from ``map.yaml``.

    Parameters
    ----------
    map_path : Path
        Path to ``map.yaml`` containing flat heading data.
    output_path : Path
        Destination ``_sidebar.md`` file.
    depth : int, optional
        Maximum heading level to include. ``1`` only adds level 1 headings.
    """

    with map_path.open("r", encoding="utf-8") as f:
        map_data: List[Dict[str, object]] = yaml.safe_load(f) or []

    lines: List[str] = []
    readme = output_path.parent / "README.md"
    if readme.exists():
        lines.append("* [Inicio](README.md)\n")

    for entry in map_data:
        level = int(entry.get("level", 1))
        if level > depth:
            continue
        indent = "  " * (level - 1)
        slug = entry.get("slug")
        title = entry.get("title")
        lines.append(f"{indent}* [{title}](/wiki/{slug}.md)\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)
