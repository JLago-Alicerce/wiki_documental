from __future__ import annotations

from pathlib import Path

from docx import Document

from .style_map import HEADINGS_RULES


def normalize_styles(doc_path: Path, out_path: Path) -> None:
    """Normalize visual styles to structured heading styles in a DOCX file."""
    document = Document(str(doc_path))
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            for style, rule in HEADINGS_RULES.items():
                if rule(run):
                    paragraph.style = style
                    break
            else:
                continue
            break
    out_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(out_path))
