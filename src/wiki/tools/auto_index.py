from __future__ import annotations

from pathlib import Path
import yaml


def load_index(index_path: Path) -> list[dict]:
    """Load index.yaml returning a list."""
    if index_path.exists():
        with index_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
    else:
        data = []
    return data


def save_index(index_path: Path, data: list[dict]) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)


def _collect_paths(data: list[dict]) -> set[str]:
    paths: set[str] = set()
    for section in data:
        for page in section.get("pages", []):
            p = page.get("path")
            if p:
                paths.add(p)
    return paths


def auto_index_missing(index_path: Path, wiki_dir: Path, *, set_visible: bool = False) -> list[str]:
    """Add markdown files missing from index.yaml under a final section.

    Returns a list of added file names.
    """
    data = load_index(index_path)
    indexed = _collect_paths(data)

    md_files = [p.name for p in wiki_dir.glob("*.md") if p.name not in {"_sidebar.md"}]
    missing = sorted(f for f in md_files if f not in indexed)
    if not missing:
        return []

    new_pages = []
    for filename in missing:
        title = Path(filename).stem.replace("-", " ").capitalize()
        new_pages.append({"title": title, "path": filename, "visible": bool(set_visible)})

    section_title = "99. Documentos no indexados"
    for section in data:
        if section.get("section") == section_title:
            section.setdefault("pages", []).extend(new_pages)
            break
    else:
        data.append({"section": section_title, "pages": new_pages})

    save_index(index_path, data)
    return missing
