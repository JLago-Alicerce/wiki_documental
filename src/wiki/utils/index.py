from __future__ import annotations

from pathlib import Path

from wiki.processing.sidebar import build_sidebar


def render_sidebar_from_index(output_path: Path) -> None:
    """Renderiza _sidebar.md usando index.yaml."""
    from wiki.cli import cfg

    index_path = Path(cfg["paths"]["work"]) / "index.yaml"
    build_sidebar(index_path, output_path.parent, absolute_links=False)
    if output_path.name != "_sidebar.md":
        (output_path.parent / "_sidebar.md").replace(output_path)
