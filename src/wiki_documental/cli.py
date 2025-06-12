import typer
from pathlib import Path
from rich.console import Console

from . import ensure_pandoc
from .config import cfg
from .processing.normalize_docx import normalize_styles
from .processing.docx_to_md import convert_docx_to_md

app = typer.Typer(add_completion=False, add_help_option=True)

__version__ = "1.0.0"


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"wiki_documental {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=_version_callback,
        is_eager=True,
        help="Show the application version and exit.",
    )
):
    """Wiki Documental CLI."""
    return


@app.command()
def full() -> None:
    """Run full wiki generation (placeholder)."""
    console = Console()
    try:
        ensure_pandoc()
    except RuntimeError as exc:
        console.print(str(exc), style="red")
        raise typer.Exit(code=1)
    console.print("Running full placeholder")


@app.command()
def reset() -> None:
    """Reset wiki state (placeholder)."""
    typer.echo("Running reset placeholder")


@app.command()
def normalize(file: Path) -> None:
    """Normalize styles in a DOCX file."""
    dest_dir = cfg["paths"]["work"] / "normalized"
    dest_dir.mkdir(parents=True, exist_ok=True)
    out_file = dest_dir / file.name
    normalize_styles(file, out_file)
    typer.echo(f"Normalized DOCX saved to {out_file}")


@app.command()
def convert(file: Path) -> None:
    """Convert DOCX to Markdown using Pandoc."""
    dest_dir = cfg["paths"]["work"] / "md_raw"
    dest_dir.mkdir(parents=True, exist_ok=True)
    out_file = dest_dir / f"{file.stem}.md"
    convert_docx_to_md(file, out_file)
    typer.echo(f"Converted markdown saved to {out_file}")
