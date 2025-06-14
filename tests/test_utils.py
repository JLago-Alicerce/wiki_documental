from wiki.utils import safe_slug


def test_safe_slug_uniqueness():
    existing = set()
    s1 = safe_slug("Título", existing)
    existing.add(s1)
    s2 = safe_slug("Título", existing)
    assert s1 != s2
    assert s2.startswith(s1 + "-")


def test_safe_slug_clean():
    slug = safe_slug("Árbol / Fase", set())
    assert slug == "arbol-fase"
