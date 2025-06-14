from wiki.processing.index_builder import build_index_from_map


def test_build_index_from_map():
    map_data = [
        {"level": 1, "title": "H1", "slug": "h1"},
        {"level": 2, "title": "H1.1", "slug": "h1-1"},
        {"level": 3, "title": "H1.1.1", "slug": "h1-1-1"},
        {"level": 1, "title": "H2", "slug": "h2"},
    ]
    result = build_index_from_map(map_data)
    assert result[0]["id"] == "1"
    assert result[0]["children"][0]["id"] == "1.1"
    assert not result[0]["children"][0]["children"]
    assert result[1]["id"] == "2"
