from docx import Document
from docx.shared import Pt

from wiki_documental.processing.normalize_docx import normalize_styles


def test_normalize_styles(tmp_path):
    sample = tmp_path / "sample.docx"
    doc = Document()
    run = doc.add_paragraph().add_run("Title")
    run.bold = True
    run.font.size = Pt(16)
    doc.add_paragraph("Body text")
    doc.save(sample)

    out = tmp_path / "out.docx"
    normalize_styles(sample, out)

    doc = Document(out)
    assert doc.paragraphs[0].style.name == "Heading 1"
    assert doc.paragraphs[1].style.name == "Normal"
