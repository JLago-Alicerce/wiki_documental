import yaml
from wiki.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_sidebar_filters(tmp_path, monkeypatch):
    index_data = [
        {"id": "1", "title": "A", "slug": "a", "children": []},
        {"id": "2", "title": "B", "slug": "fragmento_b", "children": []},
        {"id": "3", "title": "C", "slug": "c", "children": []},
        {"id": "4", "title": "D", "slug": "d" * 121, "children": []},
    ]
    (tmp_path / "index.yaml").write_text(
        yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8"
    )
    paths = {"work": tmp_path, "wiki": tmp_path}
    monkeypatch.setattr("wiki.cli.cfg", {"paths": paths})

    (tmp_path / "a.md").write_text("# Title\n", encoding="utf-8")
    (tmp_path / "fragmento_b.md").write_text("# Title\n", encoding="utf-8")
    (tmp_path / "c.md").write_text("Sin encabezado\n", encoding="utf-8")
    (tmp_path / ("d" * 121 + ".md")).write_text("# Largo\n", encoding="utf-8")

    result = runner.invoke(app, ["sidebar"])
    assert result.exit_code == 0
    sidebar = tmp_path / "_sidebar.md"
    assert sidebar.exists()
    content = sidebar.read_text(encoding="utf-8").splitlines()
    assert content == ["* [A](a.md)"]
