import yaml
from pathlib import Path
from typer.testing import CliRunner

from wiki.cli import app

runner = CliRunner()


def test_preview_command(tmp_path, monkeypatch):
    wiki_dir = tmp_path / "wiki"
    work_dir = tmp_path / "work"
    wiki_dir.mkdir()
    work_dir.mkdir()

    # Sample markdown and asset
    (wiki_dir / "a.md").write_text("# A\n", encoding="utf-8")
    assets = wiki_dir / "assets"
    assets.mkdir()
    (assets / "img.png").write_text("bin", encoding="utf-8")

    index_path = work_dir / "index.yaml"
    index_data = [{"section": "Sec", "pages": [{"title": "A", "path": "a.md", "visible": True}]}]
    index_path.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")

    monkeypatch.setattr("wiki.cli.cfg", {"paths": {"wiki": wiki_dir, "work": work_dir}})
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["preview"])
    assert result.exit_code == 0

    out_dir = tmp_path / "docs_web"
    assert (out_dir / "index.html").exists()
    assert (out_dir / "_sidebar.md").exists()
    assert (out_dir / "a.md").exists()
    assert (out_dir / "assets" / "img.png").exists()
