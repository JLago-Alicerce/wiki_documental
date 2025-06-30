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
    assert "* [1. Introducción](introduccion.md)" in sidebar_content
    assert "  * [1.1. Alcance](alcance.md)" in sidebar_content


def test_sidebar_numbers(tmp_path):
    index_file = tmp_path / "index.yaml"
    index_file.write_text(
        """
- id: '2'
  title: Sistemas
  slug: sistemas
  children:
    - id: '2.1'
      title: Servicios
      slug: servicios
      children:
        - id: '2.1.3'
          title: Interfaces SSIS
          slug: interfaces-ssis
          children: []
""",
        encoding="utf-8",
    )

    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    for slug in ["sistemas", "servicios", "interfaces-ssis"]:
        (wiki_dir / f"{slug}.md").write_text("# T\n", encoding="utf-8")

    build_sidebar(index_file, wiki_dir, absolute_links=False)

    sidebar = (wiki_dir / "_sidebar.md").read_text(encoding="utf-8")
    assert "2.1.3. Interfaces SSIS" in sidebar
