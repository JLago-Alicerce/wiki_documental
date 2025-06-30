import re
import yaml
from pathlib import Path


_HEADING_RE = re.compile(r"^#{1,6}\s+.+")


def _has_valid_title(path: Path) -> bool:
    """Devuelve ``True`` si el archivo contiene al menos un encabezado Markdown."""
    if not path.exists():
        # Si no existe, no bloquear la generación del menú
        return True

    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    i = 0
    # Saltar bloque YAML inicial si existe
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break

    # Buscar encabezado válido en las siguientes 20 líneas
    for line in lines[i : i + 20]:
        stripped = line.strip()
        if not stripped:
            continue
        if _HEADING_RE.match(stripped):
            return True
    return False


def _traverse_index(
    entries: list[dict],
    lines: list[str],
    wiki_dir: Path,
    level: int,
    absolute: bool,
    *,
    exclude_prefix: str | None,
    max_slug_len: int | None,
) -> None:
    for entry in sorted(entries, key=lambda e: str(e.get("title", "")).lower()):
        if not entry.get("visible", True):
            continue
        title = entry.get("title", "")
        slug = entry.get("slug")
        if slug and exclude_prefix and slug.startswith(exclude_prefix):
            continue
        if slug and max_slug_len and len(slug) > max_slug_len:
            continue
        if len(title.split()) > 25:
            continue
        filename = f"{slug}.md" if slug else None
        path = wiki_dir / filename if filename else None
        if not title or (path and not _has_valid_title(path)):
            continue
        indent = "  " * (level - 1)
        if len(title) > 100:
            title = title[:97].rstrip() + "..."
        display_title = (
            f"{entry['id']}. {title}"
            if str(entry.get('id', '')) and str(entry.get('id'))[0].isdigit()
            else title
        )
        if slug:
            link = f"/wiki/{filename}" if absolute else filename
            if level == 1 and lines:
                lines.append("---")
            lines.append(f"{indent}* [{display_title}]({link})")
        else:
            lines.append(f"{indent}* {display_title}")
        children = entry.get("children") or []
        _traverse_index(
            children,
            lines,
            wiki_dir,
            level + 1,
            absolute,
            exclude_prefix=exclude_prefix,
            max_slug_len=max_slug_len,
        )


def build_sidebar(
    index_path: Path,
    wiki_dir: Path,
    absolute_links: bool = False,
    *,
    exclude_prefix: str | None = "fragmento_",
    max_slug_len: int | None = 120,
) -> None:
    """Generate a Docsify sidebar from index.yaml applying simple filters."""
    with index_path.open(encoding="utf-8") as f:
        index_data = yaml.safe_load(f) or []

    # Detect new format with sections/pages
    if index_data and "section" in index_data[0]:
        converted: list[dict] = []
        for i, section in enumerate(index_data, start=1):
            sec_entry = {
                "id": str(i),
                "title": section.get("section", ""),
                "slug": None,
                "children": [],
            }
            for j, page in enumerate(section.get("pages", []), start=1):
                slug = Path(page.get("path", "")).stem
                sec_entry["children"].append(
                    {
                        "id": f"{i}.{j}",
                        "title": page.get("title", ""),
                        "slug": slug,
                        "visible": page.get("visible", True),
                        "children": [],
                    }
                )
            converted.append(sec_entry)
        index_data = converted

    def _id_is_numeric(value: str | None) -> bool:
        if not value:
            return False
        return bool(re.fullmatch(r"\d+(?:\.\d+)*", str(value)))

    def sort_entries(entries: list[dict]) -> None:
        if not all(_id_is_numeric(e.get("id")) for e in entries):
            entries.sort(key=lambda e: str(e.get("title", "")).lower())
        else:
            entries.sort(key=lambda e: [int(x) for x in str(e.get("id")).split(".")])
        for ent in entries:
            sort_entries(ent.get("children") or [])

    sort_entries(index_data)

    lines: list[str] = []
    _traverse_index(
        index_data,
        lines,
        wiki_dir,
        1,
        absolute_links,
        exclude_prefix=exclude_prefix,
        max_slug_len=max_slug_len,
    )

    sidebar_path = wiki_dir / "_sidebar.md"
    sidebar_path.parent.mkdir(parents=True, exist_ok=True)
    with sidebar_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
