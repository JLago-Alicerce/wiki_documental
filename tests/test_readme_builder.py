import yaml
from wiki_documental.processing.readme_builder import build_readme
from wiki_documental.processing.index_builder import build_index_from_map


def test_build_readme_from_files(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "2_b.md").write_text("# B", encoding="utf-8")
    (wiki / "1_a.md").write_text("# A", encoding="utf-8")

    build_readme(wiki)
    lines = (wiki / "README.md").read_text(encoding="utf-8").splitlines()
    assert lines[-2:] == ["* [A](1_a.md)", "* [B](2_b.md)"]


def test_build_readme_from_map(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "1_b.md").write_text("# B", encoding="utf-8")
    (wiki / "2_a.md").write_text("# A", encoding="utf-8")

    map_data = [
        {"level": 1, "title": "B", "slug": "b"},
        {"level": 1, "title": "A", "slug": "a"},
    ]
    map_file = tmp_path / "map.yaml"
    map_file.write_text(yaml.safe_dump(map_data, allow_unicode=True), encoding="utf-8")

    index_data = build_index_from_map(map_data)
    index_file = tmp_path / "index.yaml"
    index_file.write_text(yaml.safe_dump(index_data, allow_unicode=True), encoding="utf-8")

    build_readme(wiki, index_path=index_file, map_path=map_file)
    lines = (wiki / "README.md").read_text(encoding="utf-8").splitlines()
    assert lines[-2:] == ["* [A](2_a.md)", "* [B](1_b.md)"]

