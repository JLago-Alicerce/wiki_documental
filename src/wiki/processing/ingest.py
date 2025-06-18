from __future__ import annotations

import re
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List

from wiki.utils.slug import basic_slug

import yaml
from .md_post import (
    post_process_text,
    fix_image_links,
    warn_missing_images,
    normalize_image_paths,
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def _split_front_matter(text: str, max_lines: int = 5) -> tuple[Dict[str, Any], str]:
    """Return YAML front matter and text without that block."""
    lines = text.splitlines()
    start: int | None = None
    for i in range(min(len(lines), max_lines)):
        if lines[i].strip() == "---":
            start = i
            break
    if start is None:
        return {}, text
    end: int | None = None
    for j in range(start + 1, len(lines)):
        if lines[j].strip() == "---":
            end = j
            break
    if end is None:
        return {}, text

    meta_yaml = "\n".join(lines[start + 1 : end])
    try:
        meta = yaml.safe_load(meta_yaml) or {}
    except Exception:
        meta = {}

    remaining = "\n".join(lines[:start] + lines[end + 1 :])
    if text.endswith("\n") and not remaining.endswith("\n"):
        remaining += "\n"
    return meta, remaining


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


def _read_front_matter(path: Path) -> Dict[str, Any]:
    """Return YAML front matter dict from an existing file."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")

    comment_match = re.match(r"<!--\n---\n(.*?)\n---\n-->", text, flags=re.DOTALL)
    if comment_match:
        content = comment_match.group(1)
    elif text.startswith("---\n"):
        # Legacy style visible front matter
        end = text.find("\n---", 4)
        if end == -1:
            return {}
        content = text[4:end]
    else:
        return {}

    try:
        data = yaml.safe_load(content) or {}
    except Exception:
        data = {}
    return data


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
    unclassified_sections: List[tuple[str, List[str]]] = []
    untitled_count = 1

    for title, lines in sections:
        if title == "__intro__":
            new_title = f"Seccion sin titulo {untitled_count}"
            untitled_count += 1
            lines = [f"# {new_title}\n", "<!-- Fallback: sin correspondencia -->\n"] + list(lines)
            unclassified_sections.append((new_title, lines))
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
            if not HEADING_RE.match(lines[0]):
                new_title = f"Seccion sin titulo {untitled_count}"
                untitled_count += 1
                lines.insert(0, f"# {new_title}\n")
                sec_title = new_title
            else:
                sec_title = title
            lines.insert(1, "<!-- Fallback: sin correspondencia -->\n")
            unclassified_sections.append((sec_title, lines))

    out_dir.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        slug = entry["slug"]
        if not slug:
            continue
        text = "".join(content_map.get(slug, []))
        if not text.strip():
            continue
        path = out_dir / f"{slug}.md"

        meta = _read_front_matter(path)
        inserted = meta.get("inserted", datetime.utcnow().isoformat())

        existing_sources = meta.get("doc_source")
        sources: List[str] = []
        if isinstance(existing_sources, list):
            sources.extend(existing_sources)
        elif isinstance(existing_sources, str):
            sources.append(existing_sources)

        if doc_source is not None:
            new_src = f"{Path(doc_source).stem}.docx"
            if new_src not in sources:
                sources.append(new_src)

        _fm, body = _split_front_matter(text)
        header_lines = ["---", f"source: {md_path.name}"]
        if sources:
            if len(sources) == 1:
                header_lines.append(f"doc_source: {sources[0]}")
            else:
                header_lines.append("doc_source:")
                for s in sorted(sources):
                    header_lines.append(f"  - {s}")
        elif doc_source is not None:
            header_lines.append(f"doc_source: {Path(doc_source).stem}.docx")
        header_lines.append(f"inserted: {inserted}")
        header_lines.append("---\n")
        header = "\n".join(header_lines)
        hidden_yaml = f"<!--\n{header}-->\n\n"

        meta_parts = [f"source: {md_path.name}"]
        if sources:
            meta_parts.append("doc: " + ", ".join(sorted(sources)))
        meta_parts.append(f"inserted: {inserted}")
        meta_line = (
            f'<div class="fragment-meta">{" | ".join(meta_parts)}</div>\n\n'
        )

        body_lines = body.splitlines()
        if not any("fragment-meta" in line for line in body_lines[:5]):
            body = meta_line + body

        final_text = post_process_text(hidden_yaml + body)
        final_text = fix_image_links(final_text)
        final_text = normalize_image_paths(final_text)
        assert "assets/assets/media/" not in final_text, "\u274c Doble ruta assets detectada"
        warn_missing_images(final_text, out_dir)
        with path.open("w", encoding="utf-8") as f:
            f.write(final_text)

    if unclassified_sections:
        uc_path = out_dir / "99_unclassified.md"
        meta = _read_front_matter(uc_path)
        inserted = meta.get("inserted", datetime.utcnow().isoformat())
        existing_sources = meta.get("doc_source")
        sources: List[str] = []
        if isinstance(existing_sources, list):
            sources.extend(existing_sources)
        elif isinstance(existing_sources, str):
            sources.append(existing_sources)
        if doc_source is not None:
            new_src = f"{Path(doc_source).stem}.docx"
            if new_src not in sources:
                sources.append(new_src)

        mode = "a" if uc_path.exists() else "w"
        with uc_path.open(mode, encoding="utf-8") as f:
            if mode == "w":
                # Construir cabecera con YAML oculto
                header_lines = ["---", f"source: {md_path.name}"]
                if sources:
                    if len(sources) == 1:
                        header_lines.append(f"doc_source: {sources[0]}")
                    else:
                        header_lines.append("doc_source:")
                        for s in sorted(sources):
                            header_lines.append(f"  - {s}")
                elif doc_source is not None:
                    header_lines.append(f"doc_source: {Path(doc_source).stem}.docx")
                header_lines.append(f"inserted: {inserted}")
                header_lines.append("---\n")
                header = "\n".join(header_lines)
                hidden_yaml = f"<!--\n{header}-->\n\n"

                # Construir div de metadatos visible
                meta_parts = [f"source: {md_path.name}"]
                if sources:
                    meta_parts.append("doc: " + ", ".join(sorted(sources)))
                meta_parts.append(f"inserted: {inserted}")
                meta_line = f'<div class="fragment-meta">{" | ".join(meta_parts)}</div>\n\n'

                # Unificar y procesar la cabecera completa
                header_text = hidden_yaml + meta_line
                header_text = post_process_text(header_text)
                header_text = fix_image_links(header_text)
                header_text = normalize_image_paths(header_text)
                assert "assets/assets/media/" not in header_text, "❌ Doble ruta assets detectada"
                warn_missing_images(header_text, out_dir)
                f.write(header_text)

            # Escribir los fragmentos no clasificados
            for sec_title, section in unclassified_sections:
                sec_text = "".join(section)
                sec_text = post_process_text(sec_text)
                sec_text = fix_image_links(sec_text)
                sec_text = normalize_image_paths(sec_text)
                assert "assets/assets/media/" not in sec_text, "❌ Doble ruta assets detectada"
                warn_missing_images(sec_text, out_dir)
                f.write(sec_text)

        # Registrar los títulos de secciones no clasificadas
        log_dir = uc_path.parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        with (log_dir / "unclassified_report.txt").open("a", encoding="utf-8") as log_f:
            for sec_title, _ in unclassified_sections:
                log_f.write(basic_slug(sec_title) + "\n")