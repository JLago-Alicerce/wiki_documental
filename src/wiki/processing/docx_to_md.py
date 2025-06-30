import logging
import subprocess
from pathlib import Path
from wiki.utils.system import ensure_pandoc
from .md_post import fix_image_links, normalize_image_paths

# Configuración de logging para ver información útil durante la ejecución
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Definir constantes para mejorar la legibilidad y mantenimiento
PANDOC_CMD = "pandoc"
MARKDOWN_FORMAT = "gfm"  # GitHub Flavored Markdown
DEFAULT_MEDIA_DIR = "assets"


class PandocError(RuntimeError):
    """Excepción personalizada para errores de Pandoc."""
    pass


def convert_docx_to_md(
    docx_path: Path,
    md_path: Path,
    wiki_dir: Path | None = None,
    media_dir_name: str = DEFAULT_MEDIA_DIR,
) -> None:
    """Convierte un archivo DOCX a Markdown usando pandoc.

    Si ``wiki_dir`` está definido, los medios se extraerán a ``wiki_dir/media_dir_name``.
    """
    ensure_pandoc()

    cmd = [PANDOC_CMD, str(docx_path), "-f", "docx", "-t", MARKDOWN_FORMAT]

    if wiki_dir:
        media_path = wiki_dir / media_dir_name
        cmd.append(f"--extract-media={media_path}")

    logging.info("Ejecutando comando: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    if result.returncode != 0:
        raise PandocError(f"Error de Pandoc al convertir {docx_path}:\n{result.stderr}")

    text = result.stdout
    text = fix_image_links(text)
    text = normalize_image_paths(text)

    problematic_path = f"{media_dir_name}/{media_dir_name}/media/"
    if problematic_path in text:
        logging.warning("⚠️ Detectada doble ruta de assets: '%s'", problematic_path)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(text, encoding="utf-8")
    logging.info("✅ Archivo Markdown guardado: %s", md_path)
