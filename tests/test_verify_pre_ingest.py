import yaml
from typer.testing import CliRunner

from wiki.cli import app
from wiki.processing.verify_pre_ingest import compare_map_index

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



def test_verify_cli(tmp_path, monkeypatch):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "A", "slug": "a", "children": []}]

    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    (work / "index.yaml").write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr("wiki.cli.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 0



def test_verify_cli_with_diffs(tmp_path, monkeypatch):
    map_data = [{"level": 1, "title": "A", "slug": "a"}]
    index_data = [{"title": "B", "slug": "b", "children": []}]

    work = tmp_path
    (work / "map.yaml").write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")
    (work / "index.yaml").write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr("wiki.cli.cfg", {"paths": {"work": work}})

    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 1

