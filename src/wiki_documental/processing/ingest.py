from __future__ import annotations

import re
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List

import yaml
from .md_post import post_process_text

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def _flatten_index(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    flat: List[Dict[str, Any]] = []
    for entry in entries:
        flat.append({
            "id": entry.get("id"),
            "title": entry.get("title"),
            "slug": entry.get("slug"),
        })
        children = entry.get("children") or []
        flat.extend(_flatten_index(children))
    return flat


def _parse_sections(md_path: Path) -> List[tuple[str, List[str]]]:
    """Return list of sections split by level 1 headings."""
    sections: List[tuple[str, List[str]]] = []
    with md_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    current_title: str | None = None
    buffer: List[str] = []
    intro: List[str] = []
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            if level == 1:
                if current_title is None and intro:
                    sections.append(("__intro__", intro))
                if current_title is not None:
                    sections.append((current_title, buffer))
                current_title = m.group(2).strip()
                buffer = [line]
            else:
                if current_title is None:
                    intro.append(line)
                else:
                    buffer.append(line)
        else:
            if current_title is None:
                intro.append(line)
            else:
                buffer.append(line)
    if current_title is not None:
        sections.append((current_title, buffer))
    elif intro:
        sections.append(("__intro__", intro))
    return sections


def ingest_content(
    md_path: Path,
    index_path: Path,
    out_dir: Path,
    cutoff: float = 0.5,
    doc_source: str | Path | None = None,
) -> None:
    """Fragment markdown file according to index.yaml and store pieces."""
    with index_path.open("r", encoding="utf-8") as f:
        index_data = yaml.safe_load(f) or []
    entries = _flatten_index(index_data)

    sections = _parse_sections(md_path)

    content_map: Dict[str, List[str]] = {e["slug"]: [] for e in entries}
    unclassified: List[str] = []

    for title, lines in sections:
        if title == "__intro__":
            unclassified.extend(lines)
            continue
        best_ratio = 0.0
        best_slug: str | None = None
        for entry in entries:
            ratio = SequenceMatcher(None, title.lower(), str(entry["title"]).lower()).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_slug = entry["slug"]
        if best_slug is not None and best_ratio >= cutoff:
            content_map[best_slug].extend(lines)
        else:
            unclassified.extend(lines)

    out_dir.mkdir(parents=True, exist_ok=True)
    created = datetime.utcnow().isoformat()
    header_lines = ["---", f"source: {md_path.name}"]
    if doc_source is not None:
        header_lines.append(f"doc_source: {Path(doc_source).stem}.docx")
    header_lines.append(f"created: {created}")
    header_lines.append("---\n")
    header = "\n".join(header_lines)

    for entry in entries:
        slug = entry["slug"]
        if not slug:
            continue
        text = "".join(content_map.get(slug, []))
        if not text.strip():
            continue
        prefix = str(entry.get("id", "")).replace(".", "-")
        path = out_dir / f"{prefix}_{slug}.md"
        final_text = post_process_text(header + text)
        with path.open("w", encoding="utf-8") as f:
            f.write(final_text)

    if unclassified:
        final_text = post_process_text(header + "".join(unclassified))
        with (out_dir / "99_unclassified.md").open("w", encoding="utf-8") as f:
            f.write(final_text)
