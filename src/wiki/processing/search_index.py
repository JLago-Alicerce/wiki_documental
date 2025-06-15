import json
from pathlib import Path


def build_search_index(wiki_dir: Path, out_file: Path | None = None) -> None:
    """Genera un índice JSON para el plugin de búsqueda de Docsify."""
    index = []
    for md_file in sorted(wiki_dir.glob("*.md")):
        if md_file.name in ("_sidebar.md", "README.md"):
            continue
        content = md_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        title = ""
        for line in lines:
            if line.strip().startswith("#"):
                title = line.strip("#").strip()
                break
        index.append({
            "title": title or md_file.stem,
            "path": md_file.name,
            "body": content
        })

    out_path = out_file or (wiki_dir / "search_index.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
