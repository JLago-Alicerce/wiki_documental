from pathlib import Path
import subprocess
from wiki_documental.utils.system import ensure_pandoc


def convert_docx_to_md(docx_path: Path, md_path: Path, media_path: Path | None = None) -> None:
    """Convert DOCX to Markdown optionally extracting media files."""
    ensure_pandoc()
    cmd = ["pandoc", str(docx_path), "-f", "docx", "-t", "gfm"]
    if media_path is not None:
        cmd.append(f"--extract-media={media_path}")
    cmd.extend(["-o", str(md_path)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc error: {result.stderr}")
    text = md_path.read_text(encoding="utf-8")
    text = text.replace("media/", "assets/media/")
    md_path.write_text(text, encoding="utf-8")
