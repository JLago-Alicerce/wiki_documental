from __future__ import annotations

from pathlib import Path

import docx
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.enum.style import WD_STYLE_TYPE

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


def get_safe_heading_style(doc: Document, target_level: int) -> str:
    """Return a valid heading style name, falling back if needed."""
    target = f"Heading {target_level}"
    styles = [s.name for s in doc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]

    if target in styles:
        return target

    fallback = None
    for level in range(target_level - 1, 0, -1):
        cand = f"Heading {level}"
        if cand in styles:
            fallback = cand
            break

    if not fallback:
        fallback = "Heading 1" if "Heading 1" in styles else "Normal"

    try:
        new_style = doc.styles.add_style(target, WD_STYLE_TYPE.PARAGRAPH)
        new_style.base_style = doc.styles[fallback]
        print(f"⚠️ Estilo \"{target}\" no encontrado. Se ha clonado \"{fallback}\".")
        return target
    except Exception:
        print(f"⚠️ Estilo \"{target}\" no encontrado. Se ha usado \"{fallback}\" como sustituto.")
        return fallback


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
            safe_style = get_safe_heading_style(doc, heading_level)
            p.style = safe_style
            changes_made = True

    if changes_made:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output_path)
        print(f"\u2705 Guardado: {output_path.name}")

    return changes_made
