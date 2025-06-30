
from importlib.metadata import PackageNotFoundError, version

from .utils.system import ensure_pandoc
from .config import cfg  # noqa: F401

try:  # pragma: no cover - best effort when package isn't installed
    __version__ = version("wiki_documental")
except PackageNotFoundError:  # pragma: no cover - fallback for local use
    __version__ = "0.0.0"

