import pytest
from pathlib import Path

def test_read_write_utf8(tmp_path):
    text = "Título: ¿Qué tal? — ¡Bien! áéíóú ñ Ñ \u201cquotes\u201d"
    md = tmp_path / "sample.md"
    copy = tmp_path / "copy.md"

    md.write_text(text, encoding="utf-8")

    try:
        content = md.read_text(encoding="utf-8")
        copy.write_text(content, encoding="utf-8")
    except UnicodeDecodeError as exc:
        pytest.fail(f"Unicode error: {exc}")

    assert copy.read_text(encoding="utf-8") == text
