from __future__ import annotations

import json
import re
from pathlib import Path
from typing import List, Dict


HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def build_search_index(docs_dir: Path, out_file: Path = Path("wiki/search_index.json")) -> None:
    """Crea un índice JSON con <path, title, headings>."""
    entries: List[Dict[str, object]] = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        title: str | None = None
        headings: List[str] = []
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                match = HEADING_RE.match(line.strip())
                if not match:
                    continue
                level = len(match.group(1))
                text = match.group(2).strip()
                if level == 1 and title is None:
                    title = text
                elif level in (2, 3):
                    headings.append(text)
        if title:
            entries.append({
                "path": str(md_file.relative_to(docs_dir)),
                "title": title,
                "headings": headings,
            })
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with out_file.open("w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
