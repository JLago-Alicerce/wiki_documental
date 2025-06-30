import yaml
from wiki.processing.ingest import ingest_content


def test_discard_intro(tmp_path):
    md = tmp_path / "full.md"
    md.write_text("Presentacion del documento\n\n# Real\nTexto\n", encoding="utf-8")
    index = [{"id": "1", "title": "Real", "slug": "real", "children": []}]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True), encoding="utf-8")
    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5)
    assert (out_dir / "real.md").exists()
    assert not (out_dir / "99_unclassified.md").exists()
