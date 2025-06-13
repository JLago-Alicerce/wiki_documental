import yaml
from wiki_documental.processing.sidebar import build_sidebar


def _sample_index():
    return [
        {
            "id": "1",
            "title": "Contexto",
            "slug": "contexto",
            "children": [
                {
                    "id": "1.1",
                    "title": "Funcion",
                    "slug": "funcion",
                    "children": [
                        {
                            "id": "1.1.1",
                            "title": "Detalles",
                            "slug": "detalles",
                            "children": [],
                        }
                    ],
                }
            ],
        }
    ]


def test_build_sidebar_default_depth(tmp_path):
    index = _sample_index()
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    (tmp_path / "README.md").write_text("intro", encoding="utf-8")
    build_sidebar(index_path, out_file)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines == [
        "* [Inicio](README.md)",
        "* [Contexto](1_contexto.md)",
    ]


def test_build_sidebar_depth_3(tmp_path):
    index = _sample_index()
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    (tmp_path / "README.md").write_text("intro", encoding="utf-8")
    build_sidebar(index_path, out_file, depth=3)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "* [Inicio](README.md)"
    assert lines[1] == "* [Contexto](1_contexto.md)"
    assert lines[2] == "  * [Funcion](1-1_funcion.md)"
    assert lines[3] == "    * [Detalles](1-1-1_detalles.md)"


def test_build_sidebar_without_readme(tmp_path):
    index = _sample_index()
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")
    out_file = tmp_path / "_sidebar.md"
    build_sidebar(index_path, out_file)

    lines = out_file.read_text(encoding="utf-8").splitlines()
    assert lines == ["* [Contexto](1_contexto.md)"]
