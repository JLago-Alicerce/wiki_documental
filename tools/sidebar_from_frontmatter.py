import argparse
from pathlib import Path
from typing import Dict, Any, List
import yaml


def _read_front_matter(path: Path) -> Dict[str, Any]:
    """Return YAML front matter dict from a markdown file."""
    if not path.exists():
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return {}
    content = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(content) or {}
    except Exception:
        data = {}
    return data


def _collect_pages(root: Path) -> List[Dict[str, Any]]:
    pages: List[Dict[str, Any]] = []
    for md in root.rglob("*.md"):
        if md.name == "_sidebar.md":
            continue
        meta = _read_front_matter(md)
        if not meta:
            continue
        if meta.get("visible", True) is False:
            continue
        if meta.get("sidebar", True) is False:
            continue
        title = meta.get("title")
        raw_path = meta.get("path")
        path = Path(str(raw_path)).name if raw_path else None
        if not title or not path:
            continue
        if path == "99_unclassified.md":
            continue
        pages.append(
            {
                "section_path": meta.get("section_path", ""),
                "title": str(title),
                "path": str(path),
                "weight": int(meta.get("weight", 0)),
            }
        )
    return pages


def _build_tree(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    root: Dict[str, Any] = {"subs": {}, "pages": []}
    for page in pages:
        node = root
        sections = [s for s in str(page.get("section_path", "")).split("/") if s]
        for sec in sections:
            subs = node.setdefault("subs", {})
            node = subs.setdefault(sec, {"subs": {}, "pages": []})
        node.setdefault("pages", []).append(page)
    return root


def _render(node: Dict[str, Any], level: int = 0) -> List[str]:
    lines: List[str] = []
    indent = "  " * level
    for sec, sub in sorted(node.get("subs", {}).items()):
        lines.append(f"{indent}* {sec}")
        lines.extend(_render(sub, level + 1))
    pages = sorted(node.get("pages", []), key=lambda p: (p.get("weight", 0), p.get("title")))
    for page in pages:
        lines.append(f"{indent}* [{page['title']}]({page['path']})")
    return lines


def generate_sidebar(root: Path) -> str:
    pages = _collect_pages(root)
    tree = _build_tree(pages)
    lines = _render(tree)
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("wiki_path", type=Path)
    args = parser.parse_args()
    print(generate_sidebar(args.wiki_path))


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
