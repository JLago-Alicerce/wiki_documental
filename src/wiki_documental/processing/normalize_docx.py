from __future__ import annotations

from pathlib import Path

from docx import Document

from .style_map import HEADINGS_RULES


def _remove_toc_paragraphs(document: Document) -> None:
    """Delete paragraphs that belong to a table of contents."""
    for paragraph in list(document.paragraphs):
        style_name = paragraph.style.name if paragraph.style else ""
        if style_name.startswith("TOC") or "......" in paragraph.text:
            element = paragraph._element
            element.getparent().remove(element)


def normalize_styles(doc_path: Path, out_path: Path) -> None:
    """Normalize visual styles to structured heading styles in a DOCX file."""
    document = Document(str(doc_path))
    _remove_toc_paragraphs(document)
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
