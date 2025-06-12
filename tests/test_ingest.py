from pathlib import Path
import yaml

from wiki_documental.processing.ingest import ingest_content


def test_ingest_content(tmp_path):
    md = tmp_path / "full.md"
    md.write_text("# X\ntext1\n## Y\ntext2\n# Z\ntext3\n")

    index = [
        {"id": "1", "title": "X", "slug": "x", "children": []},
        {"id": "2", "title": "Z", "slug": "z", "children": []},
    ]
    index_path = tmp_path / "index.yaml"
    index_path.write_text(yaml.safe_dump(index, allow_unicode=True))

    out_dir = tmp_path / "wiki"
    ingest_content(md, index_path, out_dir, cutoff=0.5)

    assert (out_dir / "1_x.md").exists()
    assert (out_dir / "2_z.md").exists()
    assert (out_dir / "99_unclassified.md").exists()

