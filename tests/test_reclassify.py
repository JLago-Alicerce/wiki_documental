import yaml
from pathlib import Path
from typer.testing import CliRunner

from wiki_documental.cli import app
from wiki_documental.processing.reclassify import reclassify_unclassified


runner = CliRunner()


def _setup(tmp_path):
    work = tmp_path / "work"
    wiki = tmp_path / "wiki"
    work.mkdir()
    wiki.mkdir()
    index = [
        {"id": "1", "title": "First", "slug": "first", "children": []},
        {"id": "2", "title": "Second", "slug": "second", "children": []},
    ]
    (work / "index.yaml").write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")
    first = wiki / "1_first.md"
    first.write_text("---\n---\n# First\nold\n", encoding="utf-8")
    second = wiki / "2_second.md"
    second.write_text("---\n---\n# Second\n", encoding="utf-8")
    unclassified = wiki / "99_unclassified.md"
    unclassified.write_text("---\n---\n# First\nadd1\n# Unknown\nadd2\n", encoding="utf-8")
    return work, wiki, unclassified


def test_reclassify_unclassified(tmp_path):
    work, wiki, unclassified = _setup(tmp_path)
    reclassify_unclassified(unclassified, work / "index.yaml", wiki, threshold=0.3)
    content = (wiki / "1_first.md").read_text(encoding="utf-8")
    assert "add1" in content
    report = wiki / "report_reclassify.csv"
    assert report.exists()
    rows = report.read_text(encoding="utf-8")
    assert "Unknown" in rows


def test_reclassify_cli(tmp_path, monkeypatch):
    work, wiki, unclassified = _setup(tmp_path)
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": work, "wiki": wiki}})
    monkeypatch.setattr("wiki_documental.config.cfg", {"paths": {"work": work, "wiki": wiki}})
    result = runner.invoke(app, ["reclassify", "--threshold", "0.3"])
    assert result.exit_code == 0
    assert "add1" in (wiki / "1_first.md").read_text(encoding="utf-8")

