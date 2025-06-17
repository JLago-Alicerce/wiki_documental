import yaml
from pathlib import Path


def _traverse_index(entries: list[dict], lines: list[str], level: int, absolute: bool) -> None:
    for entry in entries:
        title = entry.get("title", "")
        slug = entry.get("slug")
        if not slug:
            continue
        filename = f"{slug}.md"
        link = f"/wiki/{filename}" if absolute else filename
        indent = "  " * (level - 1)
        lines.append(f"{indent}* [{title}]({link})")
        children = entry.get("children") or []
        _traverse_index(children, lines, level + 1, absolute)


def build_sidebar(index_path: Path, wiki_dir: Path, absolute_links: bool = False) -> None:
    """Generate a Docsify sidebar from index.yaml."""
    with index_path.open(encoding="utf-8") as f:
        index_data = yaml.safe_load(f) or []

    lines: list[str] = []
    _traverse_index(index_data, lines, 1, absolute_links)

    sidebar_path = wiki_dir / "_sidebar.md"
    sidebar_path.parent.mkdir(parents=True, exist_ok=True)
    with sidebar_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
