from __future__ import annotations

from pathlib import Path

from docx import Document

from .normalization_utils import (
    detect_heading_by_heuristics,
    detect_heading_by_style,
    should_use_heuristics,
)


def _remove_toc_paragraphs(document: Document) -> None:
    """Delete paragraphs that belong to a table of contents."""
    for paragraph in list(document.paragraphs):
        style_name = paragraph.style.name if paragraph.style else ""
        if style_name.startswith("TOC") or "......" in paragraph.text:
            element = paragraph._element
            element.getparent().remove(element)


def normalize_styles(doc_path: Path, out_path: Path, cfg: dict | None = None) -> None:
    """Normalize visual styles to structured heading styles in a DOCX file."""
    if cfg is None:  # pragma: no cover - used by CLI
        from ..config import cfg as default_cfg

        cfg = default_cfg

    document = Document(str(doc_path))
    _remove_toc_paragraphs(document)

    use_heuristics = should_use_heuristics(doc_path, cfg)

    for paragraph in document.paragraphs:
        if use_heuristics:
            level = detect_heading_by_heuristics(paragraph)
        else:
            level = detect_heading_by_style(paragraph)
        if level:
            paragraph.style = f"Heading {level}"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(out_path))
