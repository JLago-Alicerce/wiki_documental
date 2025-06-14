import hashlib
import re
import unicodedata

__all__ = ["safe_slug", "ensure_pandoc"]

from .system import ensure_pandoc


def safe_slug(title: str, existing: set[str], max_len: int = 50) -> str:
    """Return a unique, ASCII-only slug for ``title``.

    Collisions are resolved by appending a short hash suffix.
    """
    normalized = unicodedata.normalize("NFKD", title)
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    slug = slug[:max_len].rstrip("-")
    if slug in existing:
        h = hashlib.sha1(title.encode("utf-8")).hexdigest()[:4]
        slug = f"{slug}-{h}"
    return slug
