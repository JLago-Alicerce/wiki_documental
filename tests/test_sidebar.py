from wiki.processing.sidebar import build_sidebar
from pathlib import Path


def test_sidebar_generation(tmp_path):
    map_file = tmp_path / "map.yaml"
    map_file.write_text(
        """
- level: 1
  title: Introducción
  filename: 1_1-introduccion.md
- level: 2
  title: Alcance
  filename: 1_2-alcance.md
""",
        encoding="utf-8",
    )

    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    build_sidebar(map_file, wiki_dir, absolute_links=False)

    sidebar_content = (wiki_dir / "_sidebar.md").read_text(encoding="utf-8")
    assert "* [Introducción](1_1-introduccion.md)" in sidebar_content
    assert "  * [Alcance](1_2-alcance.md)" in sidebar_content
