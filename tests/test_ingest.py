from pathlib import Path
import yaml

from wiki.processing.ingest import ingest_content


def test_ingest_content(tmp_path):
    md = tmp_path / "full.md"
    md.write_text("# X\ntext1\n## Y\ntext2\n### Zeta\ntext3\n# Z\ntext4\n", encoding="utf-8")

    index = [
        {"id": "1", "title": "X", "slug": "x", "children": []},
        {"id": "2", "title": "Z", "slug": "z", "children": []},
    ]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5, doc_source="estado_actual")

    first = out_dir / "x.md"
    second = out_dir / "z.md"
    assert first.exists()
    assert second.exists()
    assert not (out_dir / "99_unclassified.md").exists()
    content = first.read_text(encoding="utf-8")
    lines = content.splitlines()
    assert lines[0] == "---"
    end = lines.index("---", 1)
    meta = yaml.safe_load("\n".join(lines[1:end]))
    assert meta["source"] == md.name
    assert meta["doc_source"] == "estado_actual.docx"
    assert lines[end + 1].startswith("<div class=\"fragment-meta\"")
    assert any(line.startswith("#") for line in lines[end + 1:])
    assert "## Y" in content
    assert "### Zeta" in content


def test_ingest_heading_clean(tmp_path):
    md = tmp_path / "full.md"
    md.write_text("# 1 Introducción <sub>a</sub>\nTexto\n", encoding="utf-8")

    index = [{"id": "1", "title": "Introducción", "slug": "introduccion", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5, doc_source="DocA")

    final = out_dir / "introduccion.md"
    assert final.exists()
    lines = final.read_text(encoding="utf-8").splitlines()
    end = lines.index("---", 1)
    body = lines[end + 1:]
    heading = next(l for l in body if l.startswith('#'))
    assert heading == '# Introducción'


def test_ingest_no_duplicate_meta(tmp_path):
    md = tmp_path / "full.md"
    md.write_text(
        "---\nsource: full.md\n---\n"
        "<div class=\"fragment-meta\">source: full.md | doc: DocA.docx | created: 2020-01-01</div>\n\n"
        "# Seccion\nTexto\n",
        encoding="utf-8",
    )

    index = [{"id": "1", "title": "Seccion", "slug": "seccion", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5, doc_source="DocA")

    final = out_dir / "seccion.md"
    assert final.exists()
    lines = final.read_text(encoding="utf-8").splitlines()
    meta_lines = [l for l in lines if '<div class="fragment-meta">' in l]
    assert len(meta_lines) == 1

