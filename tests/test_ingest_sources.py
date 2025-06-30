import yaml
from wiki.processing.ingest import ingest_content, _read_front_matter


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

    final = out_dir / "introduccion.md"
    assert final.exists()
    content = final.read_text(encoding="utf-8")
    lines = content.splitlines()
    assert lines[0] == "<!--"
    end = lines.index("-->")
    meta = _read_front_matter(final)
    assert sorted(meta["doc_source"]) == ["DocA.docx", "DocB.docx"]
    visible_line = next(l for l in lines[end + 1 :] if l.strip())
    assert visible_line.startswith("<div class=\"fragment-meta\"")
