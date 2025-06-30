import yaml
from wiki.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_sidebar_visible_flag(tmp_path, monkeypatch):
    index_data = [
        {
            "section": "Sec",
            "pages": [
                {"title": "A", "path": "a.md", "visible": True},
                {"title": "B", "path": "b.md", "visible": False},
            ],
        }
    ]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")
    paths = {"work": tmp_path, "wiki": tmp_path}
    monkeypatch.setattr("wiki.cli.cfg", {"paths": paths})

    (tmp_path / "a.md").write_text("# Title\n", encoding="utf-8")
    (tmp_path / "b.md").write_text("# Title\n", encoding="utf-8")

    result = runner.invoke(app, ["sidebar"])
    assert result.exit_code == 0
    content = (tmp_path / "_sidebar.md").read_text(encoding="utf-8").splitlines()
    assert content == ["* 1. Sec", "  * [1.1. A](a.md)"]
