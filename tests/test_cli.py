import builtins
from docx import Document
from docx.shared import Pt

from typer.testing import CliRunner

from wiki_documental.cli import app

runner = CliRunner()


def test_version_option():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "1.0.0" in result.stdout


def test_full_calls_ensure_pandoc(monkeypatch):
    called = {"value": False}

    def dummy():
        called["value"] = True

    monkeypatch.setattr("wiki_documental.cli.ensure_pandoc", dummy)
    result = runner.invoke(app, ["full"])
    assert result.exit_code == 0
    assert called["value"]
    assert "Running full placeholder" in result.stdout


def test_normalize_command(tmp_path, monkeypatch):
    sample = tmp_path / "sample.docx"
    doc = Document()
    run = doc.add_paragraph().add_run("Title")
    run.bold = True
    run.font.size = Pt(16)
    doc.add_paragraph("Text")
    doc.save(sample)

    monkeypatch.setattr(
        "wiki_documental.cli.cfg", {"paths": {"work": tmp_path}}
    )
    result = runner.invoke(app, ["normalize", str(sample)])
    assert result.exit_code == 0
    assert (tmp_path / "normalized" / sample.name).exists()

import yaml


def test_map_command(tmp_path, monkeypatch):
    md_folder = tmp_path / "md_raw"
    md_folder.mkdir()
    (md_folder / "sample.md").write_text("# Title\n")
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": tmp_path}})
    result = runner.invoke(app, ["map"])
    assert result.exit_code == 0
    map_file = tmp_path / "map.yaml"
    assert map_file.exists()
    data = yaml.safe_load(map_file.read_text())
    assert data[0]["slug"] == "title"
