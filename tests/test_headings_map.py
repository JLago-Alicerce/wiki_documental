from wiki.processing.headings_map import build_headings_map


def test_build_headings_map(tmp_path):
    md_folder = tmp_path / "md_raw"
    md_folder.mkdir()
    md_file = md_folder / "sample.md"
    md_file.write_text("# H1\n## H2\n### H3\n", encoding="utf-8")
    result = build_headings_map(md_folder)
    assert result == [
        {
            "id": "1",
            "level": 1,
            "title": "H1",
            "slug": "h1",
            "filename": "h1.md",
        },
        {
            "id": "1.1",
            "level": 2,
            "title": "H2",
            "slug": "h2",
            "filename": "h2.md",
        },
        {
            "id": "1.1.1",
            "level": 3,
            "title": "H3",
            "slug": "h3",
            "filename": "h3.md",
        },
    ]


def test_strip_numbers(tmp_path):
    md_folder = tmp_path / "md_raw"
    md_folder.mkdir()
    md_file = md_folder / "sample.md"
    md_file.write_text("# 1 Intro\n## 1.1 Segundo\n### 1.1.1 Tercero\n", encoding="utf-8")
    result = build_headings_map(md_folder)
    assert result == [
        {
            "id": "1",
            "level": 1,
            "title": "Intro",
            "slug": "intro",
            "filename": "intro.md",
        },
        {
            "id": "1.1",
            "level": 2,
            "title": "Segundo",
            "slug": "segundo",
            "filename": "segundo.md",
        },
        {
            "id": "1.1.1",
            "level": 3,
            "title": "Tercero",
            "slug": "tercero",
            "filename": "tercero.md",
        },
    ]


def test_custom_styles(tmp_path, monkeypatch):
    md_folder = tmp_path / "md_raw"
    md_folder.mkdir()
    md_file = md_folder / "sample.md"
    md_file.write_text("!! H1\n! H2\n", encoding="utf-8")

    custom_cfg = {"headings": {"styles": {"!!": 1, "!": 2}}}
    import wiki.processing.headings_map as hm

    monkeypatch.setattr(hm, "cfg", custom_cfg)
    result = hm.build_headings_map(md_folder)
    assert [r["level"] for r in result] == [1, 2]
    assert [r["slug"] for r in result] == ["h1", "h2"]
