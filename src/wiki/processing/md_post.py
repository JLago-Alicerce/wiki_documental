from __future__ import annotations

import re
from typing import List
from pathlib import Path

IMAGE_PREFIX_RE = re.compile(
    r"(!\[[^\]]*\]\()(?:\./|\.\./)*\.?/??(?:assets/)?media/"
)
IMG_TAG_PREFIX_RE = re.compile(
    r"(<img[^>]*src=\")(?:\./|\.\./)*\.?/??(?:assets/)?media/"
)


def fix_image_links(text: str) -> str:
    """Normalize media links ensuring the assets prefix."""
    text = IMAGE_PREFIX_RE.sub(r"\1assets/media/", text)
    text = IMG_TAG_PREFIX_RE.sub(r"\1assets/media/", text)
    text = re.sub(r"(assets/)+media/", "assets/media/", text)
    text = re.sub(r"(media/)+", "media/", text)
    return text


def normalize_image_paths(md_text: str) -> str:
    """Normalize image paths replacing backslashes and absolute drive paths."""

    md_text = md_text.replace("\\", "/")
    def repl(match: re.Match[str]) -> str:
        path = match.group(1)
        name = Path(path).name.replace("\\", "/")
        return f"(assets/media/{name})"

    md_text = re.sub(r"\(([a-zA-Z]:[^)]+)\)", repl, md_text)
    def repl_img(match: re.Match[str]) -> str:
        path = match.group(1)
        name = Path(path).name.replace("\\", "/")
        return f'src="assets/media/{name}"'

    md_text = re.sub(r'src="([a-zA-Z]:[^"]+)"', repl_img, md_text)
    return md_text


ASSET_LINK_RE = re.compile(r"!\[[^\]]*\]\((assets/media/[^)]+)\)")


def warn_missing_images(text: str, wiki_dir: Path) -> None:
    """Print warning for any linked images that do not exist."""
    for rel in ASSET_LINK_RE.findall(text):
        if not (wiki_dir / rel).exists():
            print(f"Warning: missing image {wiki_dir / rel}")


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_NUMBER_RE = re.compile(r"^\d+(?:\.\d+)*\s+")
_TAG_RE = re.compile(r"<[^>]+>")
_SUB_TAG_RE = re.compile(r"<sub>.*?</sub>", flags=re.I)
_SUP_TAG_RE = re.compile(r"<sup>.*?</sup>", flags=re.I)


def clean_lines(lines: List[str]) -> List[str]:
    """Clean markdown lines removing leaders and fixing heading formatting."""
    cleaned: List[str] = []
    for line in lines:
        stripped = line.rstrip("\n")
        if len(stripped) > 120 and set(stripped) == {"."}:
            # drop long leader dot lines
            continue

        m = _HEADING_RE.match(stripped)
        if m:
            level = len(m.group(1))
            prefix = m.group(1)
            title = m.group(2)
            if level > 1 and cleaned and cleaned[-1].strip() != "":
                # ensure blank line before secondary headings
                cleaned.append("\n")

            title = title.replace("**", " ")
            title = _SUB_TAG_RE.sub("", title)
            title = _SUP_TAG_RE.sub("", title)
            title = _TAG_RE.sub("", title)
            title = _NUMBER_RE.sub("", title)
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
