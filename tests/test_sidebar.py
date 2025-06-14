import yaml
from wiki.processing.sidebar import build_sidebar


def _sample_map():
    return [
        {"level": 1, "title": "Contexto", "slug": "contexto"},
        {"level": 2, "title": "Funcion", "slug": "funcion"},
        {"level": 3, "title": "Detalles", "slug": "detalles"},
    ]


def test_build_sidebar_default_depth(tmp_path):
    data = _sample_map()
    map_path = tmp_path / "map.yaml"
    map_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    (tmp_path / "README.md").write_text("intro", encoding="utf-8")
    build_sidebar(map_path, out_file)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines == [
        "* [Inicio](README.md)",
        "* [Contexto](contexto.md)",
    ]


def test_build_sidebar_depth_3(tmp_path):
    data = _sample_map()
    map_path = tmp_path / "map.yaml"
    map_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    (tmp_path / "README.md").write_text("intro", encoding="utf-8")
    build_sidebar(map_path, out_file, depth=3)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "* [Inicio](README.md)"
    assert lines[1] == "* [Contexto](contexto.md)"
    assert lines[2] == "  * [Funcion](funcion.md)"
    assert lines[3] == "    * [Detalles](detalles.md)"


def test_build_sidebar_without_readme(tmp_path):
    data = _sample_map()
    map_path = tmp_path / "map.yaml"
    map_path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    build_sidebar(map_path, out_file)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines == ["* [Contexto](contexto.md)"]
