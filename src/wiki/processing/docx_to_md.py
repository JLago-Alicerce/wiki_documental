from pathlib import Path
import subprocess
from wiki.utils.system import ensure_pandoc
from .md_post import fix_image_links, normalize_image_paths


def convert_docx_to_md(
    docx_path: Path, md_path: Path, wiki_dir: Path | None = None
) -> None:
    """Convert DOCX to Markdown optionally extracting media files."""
    ensure_pandoc()
    cmd = ["pandoc", str(docx_path), "-f", "docx", "-t", "gfm"]
    if wiki_dir is not None:
        cmd.append(f"--extract-media={wiki_dir / 'assets'}")
    cmd.extend(["-o", str(md_path)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc error: {result.stderr}")
    text = md_path.read_text(encoding="utf-8")
    text = fix_image_links(text)
    text = normalize_image_paths(text)
    assert "assets/assets/media/" not in text, "❌ Doble ruta assets detectada"
    md_path.write_text(text, encoding="utf-8")
