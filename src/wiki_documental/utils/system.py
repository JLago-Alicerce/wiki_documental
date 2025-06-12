import shutil
import subprocess


def ensure_pandoc() -> None:
    """Raise RuntimeError if pandoc is not in PATH."""
    if shutil.which("pandoc") is None:
        raise RuntimeError(
            "Pandoc executable not found. Please install pandoc and ensure it is in PATH."
        )
    result = subprocess.run(["pandoc", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc found but failed to execute.")

