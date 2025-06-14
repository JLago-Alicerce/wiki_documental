import yaml
from typer.testing import CliRunner

from wiki_documental.cli import app
from wiki_documental.processing.verify_pre_ingest import (
    compare_map_index,
    verify_pre_ingest,
)

runner = CliRunner()


def test_compare_map_index(tmp_path):
    map_data = [
        {"level": 1, "title": "H1", "slug": "h1"},
        {"level": 2, "title": "H1.1", "slug": "h1-1"},
    ]
    index_data = [
        {"title": "H1", "slug": "h1", "children": [
            {"level": 2, "title": "H1.1", "slug": "h1-1"}
        ]}
    ]
    map_file = tmp_path / "map.yaml"
    index_file = tmp_path / "index.yaml"
    map_file.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    index_file.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")

    diffs = compare_map_index(map_file, index_file)
    assert diffs == {"missing_in_index": [], "missing_in_map": []}


def test_compare_map_index_ignore_deep(tmp_path):
    map_data = [
        {"level": 1, "title": "H1", "slug": "h1"},
        {"level": 2, "title": "H1.1", "slug": "h1-1"},
        {"level": 3, "title": "H1.1.1", "slug": "h1-1-1"},
    ]
    index_data = [
        {"title": "H1", "slug": "h1", "children": [
            {"level": 2, "title": "H1.1", "slug": "h1-1"}
        ]}
    ]
    map_file = tmp_path / "map.yaml"
    index_file = tmp_path / "index.yaml"
    map_file.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    index_file.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")

    diffs = compare_map_index(map_file, index_file)
    assert diffs == {"missing_in_index": ["h1-1"], "missing_in_map": []}



def test_verify_cli(tmp_path, monkeypatch):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "A", "slug": "a", "children": []}]

    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    (work / "index.yaml").write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": work}})
    monkeypatch.setattr("wiki_documental.config.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 0



def test_verify_cli_with_diffs(tmp_path, monkeypatch):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "B", "slug": "b", "children": []}]

    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    (work / "index.yaml").write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": work}})
    monkeypatch.setattr("wiki_documental.config.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 1


def test_verify_cli_fix(tmp_path, monkeypatch):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "B", "slug": "b", "children": []}]

    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    (work / "index.yaml").write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr("wiki_documental.cli.cfg", {"paths": {"work": work}})
    monkeypatch.setattr("wiki_documental.config.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["verify", "--fix"])
    assert result.exit_code == 0
    index_result = yaml.safe_load((work / "index.yaml").read_text(encoding="utf-8"))
    assert index_result[0]["slug"] == "a"


def test_verify_pre_ingest_non_strict(tmp_path):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "B", "slug": "b", "children": []}]
    map_file = tmp_path / "map.yaml"
    index_file = tmp_path / "index.yaml"
    map_file.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    index_file.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")

    ok = verify_pre_ingest(map_file, index_file, strict=False)
    assert ok is True
