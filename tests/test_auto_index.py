import yaml
from typer.testing import CliRunner
from wiki.cli import app
from wiki.tools.auto_index import auto_index_missing

runner = CliRunner()

def test_auto_index_missing(tmp_path):
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    (wiki_dir / "a.md").write_text("# A\n", encoding="utf-8")
    (wiki_dir / "b.md").write_text("# B\n", encoding="utf-8")
    index_path = tmp_path / "index.yaml"
    data = [{"section": "Sec", "pages": [{"title": "A", "path": "a.md", "visible": True}]}]
    index_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")

    missing = auto_index_missing(index_path, wiki_dir)
    assert missing == ["b.md"]
    result = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    last = result[-1]
    assert last["section"] == "99. Documentos no indexados"
    assert any(p["path"] == "b.md" and p["visible"] is False for p in last["pages"])


def test_cli_auto_index_missing(tmp_path, monkeypatch):
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    (wiki_dir / "a.md").write_text("# A\n", encoding="utf-8")
    index_path = tmp_path / "index.yaml"
    index_path.write_text("[]", encoding="utf-8")
    monkeypatch.setattr("wiki.cli.cfg", {"paths": {"work": tmp_path, "wiki": wiki_dir}})
    result = runner.invoke(app, ["auto-index-missing", "--set-visible"])
    assert result.exit_code == 0
    data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    assert data[0]["pages"][0]["visible"] is True
