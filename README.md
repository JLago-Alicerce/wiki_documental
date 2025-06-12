# Wiki Documental

This project provides utilities for organizing and extracting information from wiki-like content.

## CLI usage

### `wiki index`

Generates `index.yaml` from the headings map. By default the index is hierarchical and contains an `id` field representing the heading position (e.g. `1`, `1.1`, `1.1.1`).

Options:

- `--overwrite` – replace an existing `index.yaml` file.
- `--flat` – create a two-level index as in previous versions.

Example hierarchical entry:

```yaml
- id: "1"
  title: Introduction
  slug: introduction
  children:
    - id: "1.1"
      title: Details
      slug: details
      children: []
```

### `wiki full`

Run the entire conversion pipeline (placeholder). It currently just checks that Pandoc is installed and prints a message.

### `wiki reset`

Reset the working directory (placeholder for future clean-up logic).

### `wiki normalize`

Normalize a DOCX file so paragraph styles are converted into proper heading styles.

Example:

```bash
wiki normalize mydoc.docx
```

### `wiki convert`

Convert a DOCX file to Markdown using Pandoc.

Example:

```bash
wiki convert mydoc.docx
```

### `wiki map`

Create `map.yaml` from the headings found in the raw Markdown files.

Example:

```bash
wiki map
```

### `wiki verify`

Check that `map.yaml` and `index.yaml` contain the same slugs. Use `--force` to continue even if differences are found.

Example:

```bash
wiki verify
```

### `wiki ingest`

Split a consolidated Markdown file into sections defined in `index.yaml`. Each section is stored in the wiki directory.

### `wiki sidebar`

Generate a `_sidebar.md` file for Docsify based on `index.yaml`.
