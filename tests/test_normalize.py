from docx import Document
from docx.shared import Pt
import logging

from wiki.processing.normalize_docx import normalize_styles


def test_normalize_styles(tmp_path):
    sample = tmp_path / "sample.docx"
    doc = Document()

    run_h1 = doc.add_paragraph().add_run("Title H1")
    run_h1.bold = True
    run_h1.font.size = Pt(16)

    run_h2 = doc.add_paragraph().add_run("Title H2")
    run_h2.bold = True
    run_h2.font.size = Pt(12)

    run_h3 = doc.add_paragraph().add_run("Title H3")
    run_h3.bold = True
    run_h3.font.size = Pt(10)

    run_h4 = doc.add_paragraph().add_run("Title H4")
    run_h4.bold = True
    run_h4.italic = True

    doc.add_paragraph("Body text")
    doc.save(sample)

    out = tmp_path / "out.docx"
    normalize_styles(sample, out)

    doc = Document(out)
    assert doc.paragraphs[0].style.name == "Heading 1"
    assert doc.paragraphs[1].style.name == "Heading 2"
    assert doc.paragraphs[2].style.name == "Heading 3"
    assert doc.paragraphs[3].style.name == "Heading 4"
    assert doc.paragraphs[4].style.name == "Normal"


def test_normalize_styles_fallback(tmp_path, caplog):
    sample = tmp_path / "sample.docx"
    doc = Document()

    run_h1 = doc.add_paragraph().add_run("HEADING ONE")
    run_h1.font.size = Pt(16)

    run_body = doc.add_paragraph().add_run("Body text")
    run_body.font.size = Pt(11)

    doc.save(sample)

    out = tmp_path / "out.docx"
    cfg = {"options": {"allow_heading_heuristics": False, "fallback_to_heuristics_for_pdf": False, "use_heuristic_headings": True}}
    caplog.set_level(logging.WARNING)
    normalize_styles(sample, out, cfg)

    assert any("Fallback heading detection" in rec.message for rec in caplog.records)

    doc = Document(out)
    assert doc.paragraphs[0].style.name.startswith("Heading")
