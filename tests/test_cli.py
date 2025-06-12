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


def test_index_overwrite(tmp_path, monkeypatch):
    map_data = [
        {"level": 1, "title": "A", "slug": "a"},
        {"level": 2, "title": "B", "slug": "b"},
        {"level": 3, "title": "C", "slug": "c"},
    ]
    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True))
    (work / "index.yaml").write_text("old")
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["index", "--overwrite"])
    assert result.exit_code == 0
    data = yaml.safe_load((work / "index.yaml").read_text())
    assert data[0]["id"] == "1"
    assert data[0]["children"][0]["children"][0]["id"] == "1.1.1"
