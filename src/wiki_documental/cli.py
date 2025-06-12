import typer
from rich.console import Console

from . import ensure_pandoc

app = typer.Typer(add_completion=False, add_help_option=True)

__version__ = "0.1.0"


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
