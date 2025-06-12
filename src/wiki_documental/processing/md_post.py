from __future__ import annotations

import re
from typing import List


_HEADING2_RE = re.compile(r"^##\s")
_HEADING3_RE = re.compile(r"^###\s")


def clean_lines(lines: List[str]) -> List[str]:
    """Clean markdown lines removing long dot leaders and fixing spacing."""
    cleaned: List[str] = []
    for line in lines:
        stripped = line.rstrip("\n")
        if len(stripped) > 120 and set(stripped) == {"."}:
            # drop long leader dot lines
            continue
        if _HEADING2_RE.match(stripped) or _HEADING3_RE.match(stripped):
            if cleaned and cleaned[-1].strip() != "":
                cleaned.append("\n")
        cleaned.append(line)
    return cleaned


def post_process_text(text: str) -> str:
    """Return cleaned text."""
    lines = text.splitlines(keepends=True)
    return "".join(clean_lines(lines))
