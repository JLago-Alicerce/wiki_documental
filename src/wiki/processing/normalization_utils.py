from __future__ import annotations

from pathlib import Path
from docx.text.paragraph import Paragraph

from .style_map import HEADINGS_RULES


def detect_heading_by_heuristics(p: Paragraph) -> int:
    """Return heading level detected using visual heuristics."""
    for run in p.runs:
        for style, rule in HEADINGS_RULES.items():
            if rule(run):
                try:
                    return int(style.split()[1])
                except (IndexError, ValueError):
                    return 0
    return 0


def detect_heading_by_style(p: Paragraph) -> int:
    """Return heading level based on explicit paragraph style."""
    name = p.style.name if p.style else ""
    if name.startswith("Heading"):
        try:
            return int(name.split()[1])
        except (IndexError, ValueError):
            return 0
    return 0


def is_converted_from_pdf(doc_path: Path) -> bool:
    """Heuristically determine if a docx originated from a PDF conversion."""
    name = doc_path.name.lower()
    parent = str(doc_path.parent).lower()
    return "pdf" in name or "pdf" in parent


def should_use_heuristics(doc_path: Path, config: dict) -> bool:
    """Decide if heading heuristics should be used for a given document."""
    opts = config.get("options", {})
    if opts.get("allow_heading_heuristics", False):
        return True
    if opts.get("fallback_to_heuristics_for_pdf", False):
        return is_converted_from_pdf(doc_path)
    return False
