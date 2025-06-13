from pathlib import Path
import re
import sys

sidebar_path = Path("wiki/_sidebar.md")
wiki_path = Path("wiki/")
broken = []

pattern = re.compile(r"\[.*?\]\((.*?)\)")
for line in sidebar_path.read_text(encoding="utf-8").splitlines():
    match = pattern.search(line)
    if match:
        target = wiki_path / match.group(1)
        if not target.exists():
            broken.append(str(target))

if broken:
    print("\u274c Enlaces rotos encontrados en el sidebar:")
    for path in broken:
        print(" -", path)
    sys.exit(1)

print("\u2705 Todos los enlaces del sidebar son v\xe1lidos.")
