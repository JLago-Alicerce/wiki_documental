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

