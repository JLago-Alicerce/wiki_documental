from wiki_documental.processing.headings_map import build_headings_map


def test_build_headings_map(tmp_path):
    md_folder = tmp_path / "md_raw"
    md_folder.mkdir()
    md_file = md_folder / "sample.md"
    md_file.write_text("# H1\n## H2\n### H3\n", encoding="utf-8")
    result = build_headings_map(md_folder)
    assert result == [
        {"level": 1, "title": "H1", "slug": "h1"},
        {"level": 2, "title": "H2", "slug": "h2"},
        {"level": 3, "title": "H3", "slug": "h3"},
    ]
