from pathlib import Path

import wiki.config as config


def test_load_config_and_init_paths(tmp_path, monkeypatch):
    root = tmp_path / "project"
    root.mkdir()
    (root / "src/wiki").mkdir(parents=True)
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
    (root / "config.yaml").write_text(config_yaml, encoding="utf-8")

    fake_file = root / "src/wiki/config.py"
    fake_file.write_text("", encoding="utf-8")
    monkeypatch.setattr(config, "__file__", str(fake_file))
    monkeypatch.setattr(config, "BASE_DIR", root)

    cfg = config.load_config()
    assert isinstance(cfg["paths"]["originals"], Path)
    for path in cfg["paths"].values():
        assert not path.exists()

    config.cfg = cfg
    config.init_paths()
    for path in cfg["paths"].values():
        assert path.exists()
