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

    first = out_dir / "1_x.md"
    second = out_dir / "2_z.md"
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
    assert meta["visible"] is True
    assert lines[end + 1].startswith("<div class=\"fragment-meta\"")
    assert any(line.startswith("#") for line in lines[end + 1:])
    assert "## Y" in content
    assert "### Zeta" in content

