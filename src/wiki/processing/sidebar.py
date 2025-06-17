import re
import yaml
from pathlib import Path


_HEADING_RE = re.compile(r"^#{1,6}\s+.+")


def _has_valid_title(path: Path) -> bool:
    """Return ``True`` if ``path`` contains a Markdown heading."""
    if not path.exists():
        return True
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    for line in lines[i:]:
        stripped = line.strip()
        if not stripped:
            continue
        return bool(_HEADING_RE.match(stripped))
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
    for entry in entries:
        title = entry.get("title", "")
        slug = entry.get("slug")
        if not slug:
            continue
        if exclude_prefix and slug.startswith(exclude_prefix):
            continue
        if max_slug_len and len(slug) > max_slug_len:
            continue
        filename = f"{slug}.md"
        path = wiki_dir / filename
        if not _has_valid_title(path):
            continue
        link = f"/wiki/{filename}" if absolute else filename
        indent = "  " * (level - 1)
        lines.append(f"{indent}* [{title}]({link})")
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
