from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Tuple

import yaml

from .index_builder import build_index_from_map


def _flatten(entries: List[Dict[str, object]]) -> List[Dict[str, object]]:
    flat: List[Dict[str, object]] = []
    for entry in entries:
        flat.append(entry)
        flat.extend(_flatten(entry.get("children") or []))
    return flat


def _read_titles_from_index(index_path: Path) -> List[Tuple[str, str]]:
    with index_path.open("r", encoding="utf-8") as f:
        index_data: List[Dict[str, object]] = yaml.safe_load(f) or []
    items: List[Tuple[str, str]] = []
    for entry in _flatten(index_data):
        slug = str(entry.get("slug"))
        title = str(entry.get("title"))
        identifier = str(entry.get("id", "")).replace(".", "-")
        file_name = f"{identifier}_{slug}.md" if identifier else f"{slug}.md"
        items.append((title, file_name))
    return items


def _read_titles_from_map(map_path: Path) -> List[Tuple[str, str]]:
    with map_path.open("r", encoding="utf-8") as f:
        map_data: List[Dict[str, object]] = yaml.safe_load(f) or []
    index = build_index_from_map(map_data)
    items: List[Tuple[str, str]] = []
    for entry in _flatten(index):
        slug = str(entry.get("slug"))
        title = str(entry.get("title"))
        identifier = str(entry.get("id", "")).replace(".", "-")
        file_name = f"{identifier}_{slug}.md" if identifier else f"{slug}.md"
        items.append((title, file_name))
    return items


def _read_titles_from_files(wiki_dir: Path) -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = []
    for md in wiki_dir.glob("*.md"):
        if md.name in {"README.md", "_sidebar.md"}:
            continue
        title = None
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.startswith("#"):
                title = line.lstrip("#").strip()
                break
        if not title:
            title = md.stem
        items.append((title, md.name))
    return items


def build_readme(wiki_dir: Path, index_path: Path | None = None, map_path: Path | None = None) -> None:
    items: List[Tuple[str, str]] = []
    if index_path and index_path.exists():
        items = _read_titles_from_index(index_path)
    elif map_path and map_path.exists():
        items = _read_titles_from_map(map_path)
    else:
        items = _read_titles_from_files(wiki_dir)

    # keep only files that actually exist
    valid: List[Tuple[str, str]] = []
    for title, file_name in items:
        if (wiki_dir / file_name).exists():
            valid.append((title, file_name))
    items = valid

    items.sort(key=lambda x: x[0].lower())

    lines = [
        "# Conocimiento Técnico Navantia",
        "",
        "Esta wiki fue generada automáticamente. Consulta el menú lateral para navegar.",
        "",
        "## Índice de documentos",
        "",
    ]
    for title, file_name in items:
        lines.append(f"* [{title}]({file_name})")

    readme_path = wiki_dir / "README.md"
    readme_path.write_text("\n".join(lines), encoding="utf-8")
