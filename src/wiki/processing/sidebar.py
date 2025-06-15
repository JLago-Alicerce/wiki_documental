import yaml
from pathlib import Path


def build_sidebar(map_path: Path, wiki_dir: Path, absolute_links: bool = False) -> None:
    """Generate a Docsify sidebar from map.yaml."""
    with map_path.open(encoding="utf-8") as f:
        headings = yaml.safe_load(f) or []

    lines = []
    for item in headings:
        level = int(item.get("level", 1))
        title = item.get("title", "")
        filename = item.get("filename")
        if not filename:
            continue
        link = f"/wiki/{filename}" if absolute_links else filename
        indent = "  " * (level - 1)
        lines.append(f"{indent}* [{title}]({link})")

    sidebar_path = wiki_dir / "_sidebar.md"
    sidebar_path.parent.mkdir(parents=True, exist_ok=True)
    with sidebar_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
