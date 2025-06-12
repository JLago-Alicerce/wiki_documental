import builtins

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
