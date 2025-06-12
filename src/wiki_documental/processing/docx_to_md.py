from pathlib import Path
import subprocess
from wiki_documental.utils.system import ensure_pandoc


def convert_docx_to_md(docx_path: Path, md_path: Path) -> None:
    ensure_pandoc()
    cmd = ["pandoc", str(docx_path), "-f", "docx", "-t", "gfm", "-o", str(md_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc error: {result.stderr}")
