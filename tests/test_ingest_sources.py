import yaml
from wiki_documental.processing.ingest import ingest_content


def test_ingest_multiple_sources(tmp_path):
    md_a = tmp_path / "a.md"
    md_a.write_text("# Introducción\nA\n", encoding="utf-8")

    md_b = tmp_path / "b.md"
    md_b.write_text("# Introducción\nB\n", encoding="utf-8")

    index = [{"id": "1", "title": "Introducción", "slug": "introduccion", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"

    ingest_content(md_a, index_path, out_dir, cutoff=0.5, doc_source="DocA")
    ingest_content(md_b, index_path, out_dir, cutoff=0.5, doc_source="DocB")

    final = out_dir / "1_introduccion.md"
    assert final.exists()
    content = final.read_text(encoding="utf-8")
    lines = content.splitlines()
    assert lines[0] == "---"
    end = lines.index("---", 1)
    meta = yaml.safe_load("\n".join(lines[1:end]))
    assert sorted(meta["doc_source"]) == ["DocA.docx", "DocB.docx"]
    assert meta["visible"] is True
    assert lines[end + 1].startswith("<div class=\"fragment-meta\"")
