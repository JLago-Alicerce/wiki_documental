from __future__ import annotations

from pathlib import Path
from statistics import mean
from docx.text.paragraph import Paragraph
from docx.document import Document

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


def average_font_size(document: Document) -> float:
    """Return the average font size (pt) in the document."""
    sizes: list[float] = []
    for p in document.paragraphs:
        for run in p.runs:
            if run.font.size:
                sizes.append(run.font.size.pt)
    return mean(sizes) if sizes else 0.0


def detect_heading_by_fallback(p: Paragraph, avg_size: float) -> int:
    """Fallback heuristic detection based on bold, size and capitalization."""
    if not p.text.strip() or avg_size <= 0:
        return 0

    runs = [r for r in p.runs if r.text.strip()]
    if not runs:
        return 0

    max_size = 0.0
    bold_count = 0
    for r in runs:
        if r.font.size and r.font.size.pt > max_size:
            max_size = r.font.size.pt
        if r.bold:
            bold_count += 1

    if max_size <= avg_size:
        return 0

    bold_ratio = bold_count / len(runs)
    if bold_ratio < 0.5 and not p.text.isupper():
        return 0

    diff = max_size - avg_size
    if diff > 4:
        return 1
    if diff > 2:
        return 2
    return 3
