from wiki.utils.slug import safe_slug


def test_safe_slug_uniqueness():
    used = set()
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento"
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento-2"
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento-3"
