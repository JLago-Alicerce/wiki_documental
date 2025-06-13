from __future__ import annotations

import re
from typing import List
from pathlib import Path

IMAGE_PREFIX_RE = re.compile(r"(!\[[^\]]*\]\()\.?/??media/")


def fix_image_links(text: str) -> str:
    """Normalize media links ensuring the assets prefix."""

    return IMAGE_PREFIX_RE.sub(r"\1assets/media/", text)


ASSET_LINK_RE = re.compile(r"!\[[^\]]*\]\((assets/media/[^)]+)\)")


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
