import yaml
from wiki_documental.processing.sidebar import build_sidebar


def test_build_sidebar(tmp_path):
    index = [
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
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True))
    out_file = tmp_path / "_sidebar.md"
    build_sidebar(index_path, out_file)

    lines = out_file.read_text().splitlines()
    assert lines[0] == "* [Inicio](README.md)"
    assert lines[1] == "* [Contexto](1_contexto.md)"
    assert lines[2] == "  * [Funcion](1-1_funcion.md)"
    assert lines[3] == "    * [Detalles](1-1-1_detalles.md)"
