import yaml
from typer.testing import CliRunner
from wiki.cli import app
from wiki.tools.auto_index import auto_index_missing, generate_index

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


def test_generate_index_basic(tmp_path, monkeypatch):
    map_path = tmp_path / "map.yaml"
    map_data = [
        {"id": "1", "level": 1, "title": "Sec", "filename": "sec.md"},
        {"id": "1.1", "level": 2, "title": "Child", "filename": "child.md"},
        {"id": "1.1.1", "level": 3, "title": "Deep", "filename": "deep.md"},
        {"id": "2", "level": 1, "title": "Hidden", "filename": "hidden.md", "visible": False},
    ]
    map_path.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")

    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    for name in ["sec.md", "child.md", "deep.md", "hidden.md", "orphan.md"]:
        (wiki_dir / name).write_text("# T\n", encoding="utf-8")

    index_path = tmp_path / "index.yaml"
    monkeypatch.setattr(
        "wiki.tools.auto_index.cfg",
        {"menu": {"depth_limit": 2, "default_visible": True, "fallback_section": "99. Documentos no indexados"}},
    )

    generate_index(map_path, wiki_dir, index_path)
    data = yaml.safe_load(index_path.read_text(encoding="utf-8"))

    assert data[0]["title"] == "Sec"
    assert any(child["title"] == "Deep" for child in data[0]["children"])
    assert data[1]["visible"] is False
    fallback = data[-1]
    assert fallback["title"] == "99. Documentos no indexados"
    assert any(p["path"] == "orphan.md" for p in fallback["children"])


def test_generate_index_alphabetical(tmp_path, monkeypatch):
    map_path = tmp_path / "map.yaml"
    map_data = [
        {"level": 1, "title": "Beta", "filename": "b.md"},
        {"level": 1, "title": "Alpha", "filename": "a.md"},
        {"level": 1, "title": "Gamma", "filename": "c.md"},
    ]
    map_path.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")

    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    for name in ["a.md", "b.md", "c.md"]:
        (wiki_dir / name).write_text("# T\n", encoding="utf-8")

    index_path = tmp_path / "index.yaml"
    monkeypatch.setattr(
        "wiki.tools.auto_index.cfg",
        {"menu": {"depth_limit": 2, "default_visible": True, "fallback_section": "99. Documentos no indexados"}},
    )

    generate_index(map_path, wiki_dir, index_path)
    titles = [entry["title"] for entry in yaml.safe_load(index_path.read_text(encoding="utf-8"))]
    assert titles == ["Alpha", "Beta", "Gamma"]
