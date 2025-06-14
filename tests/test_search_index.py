import json
from pathlib import Path
from wiki.index_builder import build_search_index


def test_build_search_index(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text("# T1\n\n## H2\n\n### H3\n", encoding="utf-8")
    out = tmp_path / "search_index.json"
    build_search_index(docs, out)
    data = json.loads(out.read_text(encoding='utf-8'))
    assert len(data) == 1
    entry = data[0]
    assert entry["path"] == "a.md"
    assert entry["title"] == "T1"
    assert entry["headings"] == ["H2", "H3"]
