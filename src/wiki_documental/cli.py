import shutil
from pathlib import Path
from shutil import rmtree
from typing import Annotated

import yaml
import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table
from wiki.index_builder import build_search_index

from . import __version__, ensure_pandoc
from . import config
from .processing.docx_to_md import convert_docx_to_md
from .processing.headings_map import build_headings_map, save_map_yaml
from .processing.index_builder import build_index_from_map
from .processing.ingest import ingest_content
from .processing.normalize_docx import normalize_styles
from .processing.reclassify import reclassify_unclassified
from .processing.sidebar import build_sidebar
from .processing.verify_pre_ingest import (
    compare_map_index,
    repair_index,
    verify_pre_ingest,
)

cfg = config.cfg

DEFAULT_CONFIG_PATH = Path("config.yaml")

app = typer.Typer(add_completion=False, add_help_option=True)


def reset_environment(cfg: dict) -> None:
    """Remove generated artifacts from wiki and work directories."""
    console = Console()
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    paths = [wiki_dir, cfg["paths"]["work"]]
    for path in paths:
        for pattern in ["*.md", "*.yaml", "*.csv"]:
            for f in Path(path).rglob(pattern):
                if f.name == "index.html":
                    continue
                f.unlink()
                console.log(f"Deleted {f}")
    media_dir = wiki_dir / "assets" / "media"
    if media_dir.exists():
        rmtree(media_dir)
        console.log(f"Removed directory {media_dir}")

    work_dir = Path(cfg["paths"]["work"])
    paths_to_clean = [
        work_dir / "md_raw",
        work_dir / "normalized",
        work_dir / "tmp",
        work_dir / "media",
    ]
    for path in paths_to_clean:
        if path.exists():
            rmtree(path)
            console.log(f"Removed directory {path}")


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
    config.init_paths()
    return


@app.command("full")
def full(
    cfg_path: Annotated[Path, typer.Option("--cfg")] = DEFAULT_CONFIG_PATH,
    depth: int = typer.Option(
        2,
        "--depth",
        "-d",
        help="Maximum heading level to include in _sidebar.md",
        show_default=True,
    ),
    relative_links: bool = typer.Option(
        True,
        "--relative-links/--absolute-links",
        help="Generate sidebar links as relative paths",
    ),
    skip_verify: Annotated[bool, typer.Option("--skip-verify")] = False,
) -> None:
    """Run full wiki generation pipeline."""
    if depth < 1:
        raise typer.BadParameter("depth must be a positive integer")
    console = Console()
    try:
        ensure_pandoc()
    except RuntimeError as exc:
        console.print(str(exc), style="red")
        raise typer.Exit(code=1)

    originals_dir = cfg["paths"]["originals"]
    docx_files = sorted(originals_dir.glob("*.docx"))
    if not docx_files:
        console.print("No DOCX files found in originals directory", style="red")
        raise typer.Exit(code=1)

    norm_dir = cfg["paths"]["work"] / "normalized"
    md_raw_dir = cfg["paths"]["work"] / "md_raw"
    tmp_dir = cfg["paths"]["tmp"]
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    console.log(f"Using wiki directory: {wiki_dir}")

    norm_dir.mkdir(parents=True, exist_ok=True)
    md_raw_dir.mkdir(parents=True, exist_ok=True)
    tmp_dir.mkdir(parents=True, exist_ok=True)
    wiki_dir.mkdir(parents=True, exist_ok=True)

    console.print("[bold]Normalizing DOCX files...[/bold]")
    for docx in track(docx_files, description="Normalize"):
        out = norm_dir / docx.name
        try:
            normalize_styles(docx, out)
        except Exception as exc:  # pragma: no cover - defensive
            console.print(f"Error normalizing {docx.name}: {exc}", style="red")
            raise typer.Exit(code=1)

    console.print("[bold]Converting DOCX to Markdown...[/bold]")
    for docx in track(norm_dir.glob("*.docx"), description="Convert"):
        out = md_raw_dir / f"{docx.stem}.md"
        try:
            convert_docx_to_md(docx, out, wiki_dir)
            console.log(f"Converted {docx.name} -> {out}")
        except Exception as exc:  # pragma: no cover - defensive
            console.print(f"Error converting {docx.name}: {exc}", style="red")
            raise typer.Exit(code=1)

    console.print("[bold]Generating consolidated markdown...[/bold]")
    tmp_full = tmp_dir / "tmp_full.md"
    with tmp_full.open("w", encoding="utf-8") as out:
        for md in sorted(md_raw_dir.glob("*.md")):
            out.write(md.read_text(encoding="utf-8"))
            out.write("\n\n")

    map_path = cfg["paths"]["work"] / "map.yaml"
    if not map_path.exists():
        console.print("[bold]Generating map...[/bold]")
        map_data = build_headings_map(md_raw_dir)
        save_map_yaml(map_data, map_path)
    else:
        with map_path.open("r", encoding="utf-8") as f:
            map_data = yaml.safe_load(f) or []

    index_path = cfg["paths"]["work"] / "index.yaml"
    if not index_path.exists():
        console.print("[bold]Generating index...[/bold]")
        index_data = build_index_from_map(map_data)
        index_path.parent.mkdir(parents=True, exist_ok=True)
        with index_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(index_data, f, allow_unicode=True)
    else:
        with index_path.open("r", encoding="utf-8") as f:
            index_data = yaml.safe_load(f) or []

    console.print("[bold]Verifying map and index...[/bold]")
    ok = verify_pre_ingest(map_path, index_path, strict=not skip_verify)
    if not ok and not skip_verify:
        console.print("[red]Differences found – aborting[/red]")
        raise typer.Exit(1)

    console.print("[bold]Ingesting content...[/bold]")
    cutoff = float(cfg.get("options", {}).get("cutoff_similarity", 0.5))

    for md in track(sorted(md_raw_dir.glob("*.md")), description="Ingest"):
        ingest_content(md, index_path, wiki_dir, cutoff=cutoff, doc_source=md.stem)

    console.print("[bold]Generating sidebar...[/bold]")
    sidebar_dest = wiki_dir / "_sidebar.md"
    build_sidebar(index_path, sidebar_dest, depth=depth, relative_links=relative_links)

    media_src = md_raw_dir / "media"
    if media_src.exists():
        dest = wiki_dir / "assets" / "media"
        double_media = dest / "media"
        if double_media.exists():
            for img in double_media.iterdir():
                shutil.move(img, dest)
            shutil.rmtree(double_media)
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(media_src, dest)

    from .processing.readme_builder import build_readme

    build_readme(wiki_dir, index_path=index_path, map_path=map_path)

    console.print(f"\N{check mark} Wiki generada correctamente en: {wiki_dir / 'index.html'}")


@app.command()
def reset() -> None:
    """Reset wiki and work directories removing generated files."""
    reset_environment(cfg)


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
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    convert_docx_to_md(file, out_file, wiki_dir)
    print(f"Saved raw markdown to {out_file}")
    typer.echo(f"Converted markdown saved to {out_file}")


@app.command()
def map() -> None:
    """Generate YAML map of markdown headings."""
    md_folder = cfg["paths"]["work"] / "md_raw"
    map_data = build_headings_map(md_folder)
    out_file = cfg["paths"]["work"] / "map.yaml"
    save_map_yaml(map_data, out_file)
    typer.echo(f"Headings map saved to {out_file}")


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

@app.command()
def verify(
    force: bool = typer.Option(False, "--force", "-f", help="Continue even if differences are found."),
    fix: bool = typer.Option(False, "--fix", help="Repair index.yaml if differences are found."),
) -> None:
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
    if fix:
        repair_index(map_path, index_path)
        console.print("index.yaml repaired")
        diffs = compare_map_index(map_path, index_path)
        if not diffs["missing_in_index"] and not diffs["missing_in_map"]:
            console.print("Map and index are consistent.")
            return
    if not force:
        raise typer.Exit(code=1)


@app.command()
def ingest(file: Path) -> None:
    """Fragment a consolidated Markdown file into wiki sections."""
    index_path = cfg["paths"]["work"] / "index.yaml"
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    cutoff = float(cfg.get("options", {}).get("cutoff_similarity", 0.5))
    doc_source = file.stem
    ingest_content(file, index_path, wiki_dir, cutoff=cutoff, doc_source=doc_source)
    typer.echo("Content ingested")


@app.command()
def sidebar(
    depth: int = typer.Option(
        1, "--depth", "-d", help="Maximum heading level to include"
    ),
    relative_links: bool = typer.Option(
        True,
        "--relative-links/--absolute-links",
        help="Generate sidebar links as relative paths",
    ),
) -> None:
    """Generate _sidebar.md for Docsify."""
    map_path = cfg["paths"]["work"] / "map.yaml"
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    output_path = wiki_dir / "_sidebar.md"
    build_sidebar(map_path, output_path, depth=depth, relative_links=relative_links)
    typer.echo("Sidebar generated")



@app.command()
def reclassify(
    threshold: float = typer.Option(0.3, "--threshold", "-t", help="Match threshold")
) -> None:
    """Reclassify sections from 99_unclassified.md."""
    wiki_dir = cfg.get("paths", {}).get("wiki", Path("wiki"))
    unclassified = wiki_dir / "99_unclassified.md"
    if not unclassified.exists():
        raise typer.Exit(code=1)
    index_path = cfg["paths"]["work"] / "index.yaml"
    reclassify_unclassified(unclassified, index_path, wiki_dir, threshold=threshold)
    typer.echo("Reclassification completed")


@app.command("build-index")
def build_index_command(
    docs_dir: Path = typer.Argument(Path("wiki"))
) -> None:
    """Generate search_index.json for docsify-search."""
    build_search_index(docs_dir, docs_dir / "search_index.json")
    typer.echo("Search index generated")


@app.command("package")
def package_static() -> None:
    """Empaqueta la wiki generada en un archivo ZIP entregable."""
    from scripts.package_static import main as pack

    pack()

