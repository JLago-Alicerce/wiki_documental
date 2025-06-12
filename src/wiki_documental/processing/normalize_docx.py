from __future__ import annotations

from pathlib import Path

from docx import Document


def normalize_styles(doc_path: Path, out_path: Path) -> None:
    """Normalize visual styles to structured heading styles in a DOCX file."""
    document = Document(str(doc_path))
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            size = run.font.size
            bold = run.bold
            if bold and size and size.pt >= 14:
                paragraph.style = "Heading 1"
                break
            if bold and size and size.pt >= 12:
                paragraph.style = "Heading 2"
                break
    out_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(out_path))
