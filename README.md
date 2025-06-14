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

Run the entire conversion pipeline from DOCX originals to a Docsify wiki.

### `wiki reset`

Remove all generated Markdown, YAML and CSV files from the `work` and `wiki` directories. The command also deletes `work/md_raw`, `work/normalized`, `work/tmp` and any `media` folders to ensure a completely clean state while preserving `index.html` and other static assets.

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

Options:

- `--depth` – maximum heading level to include in the sidebar (default `1`).
- `--relative-links/--absolute-links` – generate links without the `/wiki/` prefix (default `--relative-links`).

### Branding

You can customize the wiki's branding by editing `wiki/index.html`.
Update the `<title>` tag and `window.$docsify.name` to display your own name
and adjust the look by modifying the theme CSS if needed.

### Search

The wiki uses the `docsify-search` plugin (version 1.4.2) stored locally at
`wiki/plugins/search.min.js`. Its SHA256 hash is
`ab20792dc69dfd9cdb19479f716f69a619e577dec452739196770134dd71f297`.
