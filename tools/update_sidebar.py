import argparse
from pathlib import Path
from typing import List


def update_sidebar(sidebar_path: Path, auto_index_path: Path) -> None:
    """Replace AUTO block in sidebar with contents of auto index file."""
    lines = sidebar_path.read_text(encoding="utf-8").splitlines()
    auto_lines = auto_index_path.read_text(encoding="utf-8").splitlines()
    start = end = None
    for i, line in enumerate(lines):
        if line.strip() == "<!-- BEGIN: AUTO -->":
            start = i
        elif line.strip() == "<!-- END: AUTO -->":
            end = i
            break
    if start is None or end is None or start >= end:
        raise RuntimeError("AUTO block not found in sidebar")
    new_lines: List[str] = []
    new_lines.extend(lines[: start + 1])
    new_lines.extend(auto_lines)
    new_lines.extend(lines[end:])
    sidebar_path.write_text("\n".join(new_lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sidebar", type=Path)
    parser.add_argument("auto_index", type=Path)
    args = parser.parse_args()
    update_sidebar(args.sidebar, args.auto_index)


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
