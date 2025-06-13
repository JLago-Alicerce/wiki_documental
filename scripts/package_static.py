from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
import sys


def main() -> None:
    wiki_dir = Path("wiki")
    required = ["index.html", "_sidebar.md", "assets/media"]
    missing = [r for r in required if not (wiki_dir / r).exists()]
    if missing:
        print(f"\u274c No se puede empaquetar. Faltan: {missing}")
        sys.exit(1)

    output = Path("dist")
    output.mkdir(exist_ok=True)
    filename = output / f"wiki_documental_{datetime.now():%Y%m%d_%H%M}.zip"

    with ZipFile(filename, "w") as zipf:
        for file in wiki_dir.rglob("*"):
            if file.is_file():
                zipf.write(file, file.relative_to(wiki_dir.parent))
    print(f"\u2705 Wiki empaquetada en: {filename}")


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
