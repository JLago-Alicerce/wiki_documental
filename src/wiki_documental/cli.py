import typer
from pathlib import Path
from rich.console import Console

from . import ensure_pandoc, __version__
from .config import cfg
from .processing.normalize_docx import normalize_styles
from .processing.docx_to_md import convert_docx_to_md
from .processing.headings_map import build_headings_map, save_map_yaml
from .processing.ingest import ingest_content
from .processing.sidebar import build_sidebar
import yaml

app = typer.Typer(add_completion=False, add_help_option=True)


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


@app.command()
def map() -> None:
    """Generate YAML map of markdown headings."""
    md_folder = cfg["paths"]["work"] / "md_raw"
    map_data = build_headings_map(md_folder)
    out_file = cfg["paths"]["work"] / "map.yaml"
    save_map_yaml(map_data, out_file)
    typer.echo(f"Headings map saved to {out_file}")


from .processing.index_builder import build_index_from_map


@app.command()
def index(
    overwrite: bool = typer.Option(
        False, "--overwrite", "-o", help="Overwrite existing index.yaml"
    ),
    flat: bool = typer.Option(False, "--flat", help="Generate flat two-level index"),
) -> None:
    """Create index.yaml from map.yaml."""
    out_file = cfg["paths"]["work"] / "index.yaml"
    if out_file.exists() and not overwrite:
        typer.echo("index.yaml already exists")
        return
    map_path = cfg["paths"]["work"] / "map.yaml"
    if map_path.exists():
        with map_path.open("r", encoding="utf-8") as f:
            map_data = yaml.safe_load(f) or []
    else:
        map_data = build_headings_map(cfg["paths"]["work"] / "md_raw")

    if flat:
        index_data: list[dict] = []
        current: dict | None = None
        for item in map_data:
            if item.get("level") == 1:
                current = {"title": item["title"], "slug": item["slug"], "children": []}
                index_data.append(current)
            else:
                if current is not None:
                    current["children"].append(
                        {"level": item["level"], "title": item["title"], "slug": item["slug"]}
                    )
    else:
        index_data = build_index_from_map(map_data)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with out_file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(index_data, f, allow_unicode=True)
    typer.echo(f"Index saved to {out_file}")

from .processing.verify_pre_ingest import compare_map_index
from rich.table import Table


@app.command()
def verify(force: bool = typer.Option(False, "--force", "-f", help="Continue even if differences are found.")) -> None:
    """Verify map.yaml and index.yaml consistency."""
    map_path = cfg["paths"]["work"] / "map.yaml"
    index_path = cfg["paths"]["work"] / "index.yaml"
    diffs = compare_map_index(map_path, index_path)
    console = Console()
    if not diffs["missing_in_index"] and not diffs["missing_in_map"]:
        console.print("Map and index are consistent.")
        raise typer.Exit()

    table = Table(title="Differences")
    table.add_column("Type")
    table.add_column("Slugs")
    table.add_row("Missing in index", ", ".join(diffs["missing_in_index"]) or "-")
    table.add_row("Missing in map", ", ".join(diffs["missing_in_map"]) or "-")
    console.print(table)
    if not force:
        raise typer.Exit(code=1)


@app.command()
def ingest(file: Path) -> None:
    """Fragment a consolidated Markdown file into wiki sections."""
    index_path = cfg["paths"]["work"] / "index.yaml"
    wiki_dir = cfg["paths"]["wiki"]
    cutoff = float(cfg.get("options", {}).get("cutoff_similarity", 0.5))
    ingest_content(file, index_path, wiki_dir, cutoff=cutoff)
    typer.echo("Content ingested")


@app.command()
def sidebar() -> None:
    """Generate _sidebar.md for Docsify."""
    index_path = cfg["paths"]["work"] / "index.yaml"
    output_path = cfg["paths"]["wiki"] / "_sidebar.md"
    build_sidebar(index_path, output_path)
    typer.echo("Sidebar generated")

