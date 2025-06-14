from __future__ import annotations

import re
from typing import List
from pathlib import Path

IMAGE_PREFIX_RE = re.compile(r"(!\[[^\]]*\]\()\.?/??(?:assets/)?media/")


def fix_image_links(text: str) -> str:
    """Normalize media links ensuring the assets prefix."""
    text = IMAGE_PREFIX_RE.sub(r"\1assets/media/", text)
    text = re.sub(r"(assets/)+media/", "assets/media/", text)
    text = re.sub(r"(media/)+", "media/", text)
    return text


def normalize_image_paths(md_text: str) -> str:
    """Normalize image paths replacing backslashes and absolute drive paths.

    Absolute drive paths like ``C:/foo/bar.png`` are rewritten to use a
    relative ``../media/imagenes/`` prefix so the links remain portable.
    """

    md_text = md_text.replace("\\", "/")

    def repl(match: re.Match[str]) -> str:
        path = match.group(1)
        name = Path(path).name.replace("\\", "/")
        return f"(../media/imagenes/{name})"

    md_text = re.sub(r"\(([a-zA-Z]:[^)]+)\)", repl, md_text)
    return md_text


ASSET_LINK_RE = re.compile(
    r"!\[[^\]]*\]\(((?:assets/media|\.\./media/imagenes)/[^)]+)\)"
)


def warn_missing_images(text: str, wiki_dir: Path) -> None:
    """Print warning for any linked images that do not exist."""
    for rel in ASSET_LINK_RE.findall(text):
        if not (wiki_dir / rel).exists():
            print(f"Warning: missing image {wiki_dir / rel}")


_HEADING2_RE = re.compile(r"^##\s")
_HEADING3_RE = re.compile(r"^###\s")


def clean_lines(lines: List[str]) -> List[str]:
    """Clean markdown lines removing leaders and fixing heading formatting."""
    cleaned: List[str] = []
    for line in lines:
        stripped = line.rstrip("\n")
        if len(stripped) > 120 and set(stripped) == {"."}:
            # drop long leader dot lines
            continue
        if _HEADING2_RE.match(stripped) or _HEADING3_RE.match(stripped):
            # ensure blank line before secondary headings
            if cleaned and cleaned[-1].strip() != "":
                cleaned.append("\n")
            # normalize heading text
            parts = stripped.split(maxsplit=1)
            prefix = parts[0]
            title = parts[1] if len(parts) > 1 else ""
            title = title.replace("**", " ")
            title = re.sub(r"\s+", " ", title).strip()
            line = f"{prefix} {title}\n"
        cleaned.append(line)
    return cleaned


def clean_markdown(text: str) -> str:
    """Return cleaned markdown text."""
    lines = text.splitlines(keepends=True)
    return "".join(clean_lines(lines))


def post_process_text(text: str) -> str:
    """Backward compatible alias for :func:`clean_markdown`."""
    return clean_markdown(text)
