from __future__ import annotations

from pathlib import Path
import logging
import yaml

from wiki.config import cfg

logger = logging.getLogger(__name__)


def load_map(path: Path) -> list[dict]:
    """Load map.yaml returning a list of nodes."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def save_index(tree: list[dict], output_path: Path) -> None:
    """Write index.yaml safely, replacing the existing file."""
    tmp = output_path.with_suffix(".tmp")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tmp.open("w", encoding="utf-8") as f:
        yaml.safe_dump(tree, f, allow_unicode=True)
    tmp.replace(output_path)


def _iter_nodes(nodes: list[dict]):
    for n in nodes:
        yield n
        for c in _iter_nodes(n.get("children") or []):
            yield c


def build_tree(map_items: list[dict], depth_limit: int) -> tuple[list[dict], dict]:
    """Build hierarchical index data from map items respecting depth_limit."""
    default_visible = cfg.get("menu", {}).get("default_visible", True)
    tree: list[dict] = []
    stack: list[tuple[int, dict]] = []
    truncated = 0
    hidden = 0

    for item in map_items:
        level = int(item.get("level", 1))
        visible = item.get("visible", default_visible)
        if not visible:
            hidden += 1
        node = {
            "title": item.get("title", ""),
            "path": item.get("filename", ""),
            "visible": bool(visible),
            "children": [],
        }
        if level > depth_limit:
            level = depth_limit
            truncated += 1
        while stack and stack[-1][0] >= level:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(node)
        else:
            tree.append(node)
        stack.append((level, node))

    stats = {"processed": len(map_items), "truncated": truncated, "hidden": hidden}
    return tree, stats


# ---------------------------------------------------------------------------
# Utility for auto-indexing orphan markdown files
# ---------------------------------------------------------------------------

def load_index(index_path: Path) -> list[dict]:
    """Load index.yaml returning a list."""
    if index_path.exists():
        with index_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
    else:
        data = []
    return data


def _collect_paths(data: list[dict]) -> set[str]:
    paths: set[str] = set()
    for section in data:
        for page in section.get("pages", []):
            p = page.get("path")
            if p:
                paths.add(p)
    return paths


def auto_index_missing(index_path: Path, wiki_dir: Path, *, set_visible: bool = False) -> list[str]:
    """Add markdown files missing from index.yaml under a final section."""
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

    section_title = cfg.get("menu", {}).get("fallback_section", "99. Documentos no indexados")
    for section in data:
        if section.get("section") == section_title:
            section.setdefault("pages", []).extend(new_pages)
            break
    else:
        data.append({"section": section_title, "pages": new_pages})

    save_index(data, index_path)
    return missing


def generate_index(map_path: Path, wiki_dir: Path, out_path: Path) -> None:
    """Create index.yaml from map.yaml using repo configuration."""
    menu_cfg = cfg.get("menu", {})
    depth_limit = int(menu_cfg.get("depth_limit", 99))
    fallback_section = menu_cfg.get("fallback_section", "99. Documentos no indexados")
    default_visible = bool(menu_cfg.get("default_visible", True))

    map_items = load_map(map_path)
    tree, stats = build_tree(map_items, depth_limit)

    indexed_paths = {n.get("path") for n in _iter_nodes(tree) if n.get("path")}
    md_files = [p.name for p in wiki_dir.glob("*.md") if p.name not in {"_sidebar.md"}]
    leftovers = sorted(f for f in md_files if f not in indexed_paths)
    if leftovers:
        pages = []
        for filename in leftovers:
            title = Path(filename).stem.replace("-", " ").capitalize()
            pages.append({"title": title, "path": filename, "visible": default_visible})
        tree.append({"title": fallback_section, "path": "", "visible": True, "children": pages})

    missing_files: list[str] = []
    for node in _iter_nodes(tree):
        path = node.get("path")
        if path:
            file_path = wiki_dir / path
            if not file_path.exists():
                node["note"] = "missing file"
                missing_files.append(path)

    save_index(tree, out_path)

    logger.info("Total de nodos procesados: %s", stats["processed"])
    logger.info("Truncados por profundidad: %s", stats["truncated"])
    logger.info("Ocultos (visible: false): %s", stats["hidden"])
    for name in missing_files:
        logger.info("Archivo no encontrado: %s", name)
