from wiki.processing.sidebar import build_sidebar


def test_sidebar_generation(tmp_path):
    index_file = tmp_path / "index.yaml"
    index_file.write_text(
        """
- id: '1'
  title: Introducción
  slug: introduccion
  children:
    - id: '1.1'
      title: Alcance
      slug: alcance
      children: []
""",
        encoding="utf-8",
    )

    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    build_sidebar(index_file, wiki_dir, absolute_links=False)

    sidebar_content = (wiki_dir / "_sidebar.md").read_text(encoding="utf-8")
    assert "* [Introducción](introduccion.md)" in sidebar_content
    assert "  * [Alcance](alcance.md)" in sidebar_content
