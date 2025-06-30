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


def test_normalize_styles_missing_style(tmp_path):
    sample = tmp_path / "sample.docx"
    doc = Document()
    run = doc.add_paragraph().add_run("H4 Title")
    run.bold = True
    run.italic = True
    doc.save(sample)

    # Remove Heading 4 style to force fallback
    doc2 = Document(sample)
    style = doc2.styles["Heading 4"]
    doc2.styles.element.remove(style._element)
    doc2.save(sample)

    out = tmp_path / "out.docx"
    normalize_styles(sample, out)

    doc_out = Document(out)
    assert doc_out.paragraphs[0].style.name.startswith("Heading")


def test_normalize_nav_styles(tmp_path):
    sample = tmp_path / "nav.docx"
    doc = Document()
    from docx.enum.style import WD_STYLE_TYPE
    doc.styles.add_style("Nav_Tit_1", WD_STYLE_TYPE.PARAGRAPH)
    doc.styles.add_style("Nav_Tit_2", WD_STYLE_TYPE.PARAGRAPH)
    doc.styles.add_style("Nav_Tit_3", WD_STYLE_TYPE.PARAGRAPH)
    doc.add_paragraph("Uno", style="Nav_Tit_1")
    doc.add_paragraph("Dos", style="Nav_Tit_2")
    doc.add_paragraph("Tres", style="Nav_Tit_3")
    doc.save(sample)

    out = tmp_path / "out.docx"
    normalize_styles(sample, out)

    doc_out = Document(out)
    assert [p.style.name for p in doc_out.paragraphs[:3]] == [
        "Heading 1",
        "Heading 2",
        "Heading 3",
    ]
