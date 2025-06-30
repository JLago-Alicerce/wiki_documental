import yaml
from wiki.processing.ingest import ingest_content, insert_section_numbers


def test_insert_numbers(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("# Intro\nTexto\n", encoding="utf-8")

    index = [{"id": "1", "title": "Intro", "slug": "intro", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5, doc_source="Doc")
    insert_section_numbers(index, out_dir)
    content = (out_dir / "intro.md").read_text(encoding="utf-8")
    assert "# 1. Intro" in content


def test_no_duplicate_front_matter(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("---\ntitle: X\n---\n# Intro\n", encoding="utf-8")

    index = [{"id": "1", "title": "Intro", "slug": "intro", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5, doc_source="Doc")
    text = (out_dir / "intro.md").read_text(encoding="utf-8")
    assert text.count("---") == 2
