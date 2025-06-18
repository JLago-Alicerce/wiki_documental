import re
import unicodedata


def basic_slug(text: str) -> str:
    """Return an ASCII slug with simple normalization."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def safe_slug(text: str, used: set[str]) -> str:
    """Generate a unique slug for ``text`` avoiding collisions in ``used``."""
    base = basic_slug(text)
    slug = base
    count = 1
    while slug in used:
        count += 1
        slug = f"{base}-{count}"
    used.add(slug)
    return slug


def slug_to_label(slug: str) -> str:
    """Return a human friendly label derived from ``slug``."""
    slug = re.sub(r"^[0-9]+-", "", slug)
    words = slug.split("-")
    return " ".join(w.capitalize() for w in words if w)
