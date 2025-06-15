from __future__ import annotations

from difflib import SequenceMatcher
from pathlib import Path
import csv
from typing import Any, Dict, List

import yaml

from .ingest import _flatten_index, _parse_sections


def reclassify_unclassified(
    unclassified_path: Path,
    index_path: Path,
    wiki_dir: Path,
    threshold: float = 0.3,
    report_path: Path | None = None,
) -> None:
    """Reclassify sections from ``unclassified_path`` using ``index_path``.

    Blocks matching a title in the index above ``threshold`` are appended to the
    corresponding markdown file. Unmatched blocks are written to ``report_path``
    as CSV with columns ``title`` and ``content``.
    """

    with index_path.open("r", encoding="utf-8") as f:
        index_data = yaml.safe_load(f) or []
    entries = _flatten_index(index_data)

    sections = _parse_sections(unclassified_path)

    if report_path is None:
        report_path = unclassified_path.parent / "report_reclassify.csv"

    unmatched: List[dict[str, str]] = []

    for title, lines in sections:
        if title == "__intro__":
            continue
        best_ratio = 0.0
        best_entry: Dict[str, Any] | None = None
        for entry in entries:
            ratio = SequenceMatcher(
                None, title.lower(), str(entry.get("title", "")).lower()
            ).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_entry = entry
        if best_entry and best_ratio >= threshold and best_entry.get("slug"):
            md_file = wiki_dir / f"{best_entry['slug']}.md"
            md_file.parent.mkdir(parents=True, exist_ok=True)
            with md_file.open("a", encoding="utf-8") as f:
                if lines and not lines[-1].endswith("\n"):
                    lines[-1] += "\n"
                f.writelines(lines)
        else:
            unmatched.append({"title": title, "content": "".join(lines)})

    if unmatched:
        with report_path.open("w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["title", "content"])
            writer.writeheader()
            writer.writerows(unmatched)
