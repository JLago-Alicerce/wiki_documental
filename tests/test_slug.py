from wiki.utils.slug import safe_slug, slug_to_label


def test_safe_slug_uniqueness():
    used = set()
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento"
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento-2"
    assert safe_slug("T\u00edtulo con acento", used) == "titulo-con-acento-3"


def test_slug_to_label():
    assert slug_to_label("01-introduccion-basica") == "Introduccion Basica"
    assert slug_to_label("abc-de-fg") == "Abc De Fg"
