from pathlib import Path
from PIL import Image
from wiki.tools.preprocess_documents import process_pdf_with_ocr
from docx import Document


def test_process_pdf_with_ocr_include_images(tmp_path, monkeypatch):
    pdf = tmp_path / "file.pdf"
    pdf.write_bytes(b"%PDF-1.4\n%%EOF")

    pages = [Image.new("RGB", (10, 10), color=i) for i in range(2)]
    monkeypatch.setattr(
        "wiki.tools.preprocess_documents.convert_from_path", lambda path: pages
    )
    monkeypatch.setattr(
        "wiki.tools.preprocess_documents.image_to_string", lambda img: "text"
    )

    out_dir = tmp_path / "out"
    process_pdf_with_ocr(pdf, out_dir, include_images=True)

    docx_path = out_dir / f"{pdf.stem}.docx"
    assert docx_path.exists()
    assert (out_dir / "assets" / "pagina_01.png").exists()
    doc = Document(docx_path)
    assert len(doc.inline_shapes) == 2


def test_process_pdf_with_ocr_without_images(tmp_path, monkeypatch):
    pdf = tmp_path / "file.pdf"
    pdf.write_bytes(b"%PDF-1.4\n%%EOF")

    pages = [Image.new("RGB", (10, 10), color=i) for i in range(1)]
    monkeypatch.setattr(
        "wiki.tools.preprocess_documents.convert_from_path", lambda path: pages
    )
    monkeypatch.setattr(
        "wiki.tools.preprocess_documents.image_to_string", lambda img: "text"
    )

    out_dir = tmp_path / "out2"
    process_pdf_with_ocr(pdf, out_dir, include_images=False)

    docx_path = out_dir / f"{pdf.stem}.docx"
    assert docx_path.exists()
    doc = Document(docx_path)
    assert len(doc.inline_shapes) == 0
