from pathlib import Path

import wiki_documental.config as config


def test_load_config_creates_directories(tmp_path, monkeypatch):
    root = tmp_path / "project"
    root.mkdir()
    (root / "src/wiki_documental").mkdir(parents=True)
    config_yaml = (
        "paths:\n"
        "  originals: 'inputs/_originals'\n"
        "  work: 'work'\n"
        "  wiki: 'wiki'\n"
        "  tmp: 'work/tmp'\n"
        "\n"
        "options:\n"
        "  ocr: false\n"
        "  cutoff_similarity: 0.5\n"
    )
    (root / "config.yaml").write_text(config_yaml)

    fake_file = root / "src/wiki_documental/config.py"
    fake_file.write_text("")
    monkeypatch.setattr(config, "__file__", str(fake_file))

    cfg = config.load_config()
    assert isinstance(cfg["paths"]["originals"], Path)
    for path in cfg["paths"].values():
        assert path.exists()
