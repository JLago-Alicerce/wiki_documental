from __future__ import annotations

from typing import Callable
from docx.text.run import Run

# Mapping of heading styles to detection rules
HEADINGS_RULES: dict[str, Callable[[Run], bool]] = {
    "Heading 1": lambda run: bool(run.bold) and run.font.size and run.font.size.pt >= 14,
    "Heading 2": lambda run: bool(run.bold) and run.font.size and run.font.size.pt >= 12,
    "Heading 3": lambda run: bool(run.bold) and run.font.size and run.font.size.pt >= 10,
    "Heading 4": lambda run: bool(run.bold) and bool(run.italic),
}
