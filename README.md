# Wiki Documental

Wiki Documental provides an automated workflow for turning a collection of DOCX files into a static wiki powered by **Docsify**.

## Features

- Normalize DOCX styles before conversion.
- Convert documents to Markdown with Pandoc extracting images.
- Generate a hierarchical `map.yaml` and `index.yaml` from headings.
- Verify map and index consistency.
- Ingest consolidated Markdown into per-section files with YAML front matter.
- Post process Markdown to clean formatting and fix image paths.
- Create a Docsify `_sidebar.md` from the index.
- Reclassify leftover content from `99_unclassified.md`.
- Package the final wiki into a ZIP archive.

## Installation

```bash
poetry install --with dev
```

## Quick start

Place your source `.docx` files in `inputs/_originals/` and run the full pipeline:

```bash
poetry run wiki full
```

The generated wiki will be placed in the `wiki/` directory. Open `wiki/index.html` in your browser to browse the result.

## Directory layout

- `inputs/_originals/` – original DOCX documents.
- `work/` – intermediate files such as `md_raw`, `map.yaml` and `index.yaml`.
- `wiki/` – final Markdown files and Docsify assets.
- `docs/` – additional documentation (see `docs/arquitectura.md`).

## CLI reference

### `wiki index`
Generate `index.yaml` from the headings map. Options:

- `--overwrite` – replace an existing index.
- `--flat` – create a two-level index.

### `wiki full`
Run the entire conversion pipeline from DOCX originals to the final wiki.

### `wiki reset`
Remove generated Markdown, YAML and CSV files from `work` and `wiki`.

### `wiki normalize`
Normalize a DOCX file so paragraph styles become proper heading levels.

```bash
poetry run wiki normalize mydoc.docx
```

### `wiki convert`
Convert a single DOCX file to Markdown using Pandoc.

```bash
poetry run wiki convert mydoc.docx
```

### `wiki map`
Create `map.yaml` from the headings found in the raw Markdown files.

### `wiki verify`
Check that `map.yaml` and `index.yaml` contain the same slugs. Use `--force` to continue even if differences are found.

### `wiki ingest`
Split a consolidated Markdown file into sections defined in `index.yaml`.

### `wiki sidebar`
Generate a `_sidebar.md` file for Docsify based on `index.yaml`.

### `wiki reclassify`
Try to relocate blocks stored in `99_unclassified.md` back into their section files.

### `wiki package`
Create a ZIP file with the wiki contents in the `dist/` directory.

## Testing

Run the automated test suite with:

```bash
poetry run pytest -q
```

## Example sidebar entry

```markdown
* [Introducción](1_1-introduccion.md)
  * [Alcance](1_2-alcance.md)
```

## Branding

You can customise the wiki's appearance by editing `wiki/index.html`. Update the `<title>` tag and `window.$docsify.name` to display your own project name.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
