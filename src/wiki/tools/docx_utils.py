from __future__ import annotations

from pathlib import Path

import docx
from docx.document import Document
from docx.text.paragraph import Paragraph

# Heuristic thresholds for heading detection
HEADING_1_MIN_FONT_SIZE = 14  # pt
HEADING_2_MIN_FONT_SIZE = 12


def is_likely_heading(p: Paragraph) -> int:
    """Return heading level detected using simple visual heuristics."""
    text = p.text.strip()
    if not text:
        return 0

    if len(text.split()) > 12:
        return 0

    base_score = 1 if text.isupper() or text[0].isupper() else 0

    bold_runs = [r.bold for r in p.runs if r.text.strip()]
    if bold_runs:
        bold_ratio = sum(1 for b in bold_runs if b) / len(bold_runs)
        if bold_ratio >= 0.5:
            base_score += 1

    for r in p.runs:
        if r.text.strip() and r.font.size:
            if r.font.size.pt >= HEADING_1_MIN_FONT_SIZE:
                return 1
            if r.font.size.pt >= HEADING_2_MIN_FONT_SIZE:
                return max(base_score, 1)
    return 1 if base_score >= 2 else 0


def clean_docx_styles(doc_path: Path, output_path: Path) -> bool:
    """Normalize paragraphs to Heading styles if they look like titles."""
    try:
        doc: Document = docx.Document(doc_path)
    except Exception as e:  # pragma: no cover - defensive
        print(f"\u274c No se pudo abrir {doc_path.name}: {e}")
        return False

    changes_made = False
    for p in doc.paragraphs:
        if p.style.name.startswith("Heading"):
            continue
        heading_level = is_likely_heading(p)
        if heading_level > 0:
            print(f"  -> '{p.text[:50].strip()}' \u2192 Heading {heading_level}")
            p.style = f"Heading {heading_level}"
            changes_made = True

    if changes_made:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output_path)
        print(f"\u2705 Guardado: {output_path.name}")

    return changes_made
