from pathlib import Path
from docx import Document
from wiki.processing.docx_to_md import convert_docx_to_md


def _create_sample_docx(path: Path, text: str) -> None:
    doc = Document()
    doc.add_paragraph(text)
    doc.save(path)


def test_convert_docx_to_md(tmp_path, monkeypatch):
    docx_file = tmp_path / "sample.docx"
    md_file = tmp_path / "sample.md"
    _create_sample_docx(docx_file, "Hello")

    def fake_run(cmd, capture_output=True, text=True):
        md_file.write_text("Hello", encoding="utf-8")
        class Result:
            returncode = 0
            stderr = ""
        return Result()

    monkeypatch.setattr("subprocess.run", fake_run)
    monkeypatch.setattr(
        "wiki.processing.docx_to_md.ensure_pandoc", lambda: None
    )
    convert_docx_to_md(docx_file, md_file)
    assert md_file.exists()
    assert md_file.read_text(encoding="utf-8") == "Hello"
