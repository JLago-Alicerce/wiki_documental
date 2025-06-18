from __future__ import annotations

from pathlib import Path

try:  # pragma: no cover - optional dependency
    from pdf2docx import Converter
except Exception:  # pragma: no cover - if pdf2docx missing
    Converter = None  # type: ignore

try:  # pragma: no cover - optional dependency
    from pdf2image import convert_from_path
except Exception:  # pragma: no cover - if pdf2image missing
    convert_from_path = None  # type: ignore

try:  # pragma: no cover - optional dependency
    from pytesseract import image_to_string
except Exception:  # pragma: no cover - if pytesseract missing
    image_to_string = None  # type: ignore


def convert_pdf_to_docx(pdf_path: Path, output_docx_path: Path) -> None:
    """Convert PDF to DOCX using pdf2docx."""
    if Converter is None:
        raise ImportError("pdf2docx is not installed")
    print(f"🧪 Intentando conversión directa para {pdf_path.name}")
    converter = Converter(str(pdf_path))
    converter.convert(str(output_docx_path), start=0, end=None)
    converter.close()


def ocr_pdf_to_markdown(pdf_path: Path, output_dir: Path) -> None:
    """Extract text from PDF using OCR and save as Markdown with images."""
    if convert_from_path is None or image_to_string is None:
        raise ImportError("pdf2image and pytesseract are required for OCR")
    print(f"🧠 Ejecutando OCR para {pdf_path.name}")
    pages = convert_from_path(str(pdf_path))
    output_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = output_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / f"{pdf_path.stem}.md"
    with md_path.open("w", encoding="utf-8") as md:
        for idx, img in enumerate(pages, start=1):
            text = image_to_string(img)
            md.write(f"## P\u00E1gina {idx}\n\n")
            md.write(text.strip() + "\n\n")
            img_name = f"{pdf_path.stem}_page_{idx:03}.png"
            img_path = assets_dir / img_name
            img.save(img_path)
            md.write(f"![P\u00E1gina {idx}](assets/{img_name})\n\n")
