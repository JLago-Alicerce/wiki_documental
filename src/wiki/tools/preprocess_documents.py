from pathlib import Path
import docx
from docx.document import Document
from docx.text.paragraph import Paragraph
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
from yaml import safe_load

# --- Heurísticas de detección de encabezados ---
HEADING_1_MIN_FONT_SIZE = 14  # pt
HEADING_2_MIN_FONT_SIZE = 12


def is_likely_heading(p: Paragraph) -> int:
    text = p.text.strip()
    if not text:
        return 0

    if len(text.split()) > 12:
        return 0

    if text.isupper() or text[0].isupper():
        base_score = 1
    else:
        base_score = 0

    bold_runs = [r.bold for r in p.runs if r.text.strip()]
    if bold_runs:
        bold_ratio = sum(1 for b in bold_runs if b) / len(bold_runs)
        if bold_ratio >= 0.5:
            base_score += 1

    for r in p.runs:
        if r.text.strip() and r.font.size:
            if r.font.size.pt >= 13:
                base_score += 1
                break

    return 1 if base_score >= 2 else 0


def clean_docx_styles(doc_path: Path, output_path: Path) -> bool:
    try:
        doc: Document = docx.Document(doc_path)
    except Exception as e:
        print(f"\u274c No se pudo abrir {doc_path.name}: {e}")
        return False

    changes_made = False
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading'):
            continue
        heading_level = is_likely_heading(p)
        if heading_level > 0:
            print(f"  → '{p.text[:50].strip()}' → Heading {heading_level}")
            p.style = f'Heading {heading_level}'
            changes_made = True

    if changes_made:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output_path)
        print(f"\u2705 Guardado: {output_path.name}")
    return changes_made


def process_pdf_with_converter(pdf_path: Path, output_docx_path: Path) -> None:
    """Convertir PDF a DOCX usando pdf2docx."""
    if Converter is None:
        raise ImportError("pdf2docx is not installed")
    print(f"🧪 Intentando conversión directa para {pdf_path.name}")
    converter = Converter(str(pdf_path))
    converter.convert(str(output_docx_path), start=0, end=None)
    converter.close()


def process_pdf_with_ocr(pdf_path: Path, output_dir: Path) -> None:
    """Extrae texto e imágenes de un PDF usando OCR."""
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
            md.write(f"## P\xE1gina {idx}\n\n")
            md.write(text.strip() + "\n\n")
            img_name = f"{pdf_path.stem}_page_{idx:03}.png"
            img_path = assets_dir / img_name
            img.save(img_path)
            md.write(f"![P\xE1gina {idx}](assets/{img_name})\n\n")


def batch_process_directory(input_dir: Path, output_dir: Path, cfg: dict | None = None):
    print(f"\n\U0001f4c2 Procesando documentos desde: {input_dir}")
    ocr_enabled = False
    ocr_dir = output_dir.parent / "ocr_outputs"
    if cfg:
        ocr_enabled = cfg.get("options", {}).get("ocr", False)
        ocr_dir = Path(cfg["paths"].get("work", output_dir.parent)) / "ocr_outputs"
    for file in sorted(input_dir.glob("*")):
        print(f"\n\U0001f4dd {file.name}")
        output_file = output_dir / (file.stem + ".docx")

        if file.suffix.lower() == ".docx":
            clean_docx_styles(file, output_file)

        elif file.suffix.lower() == ".pdf":
            try:
                if ocr_enabled:
                    raise RuntimeError("Forzando OCR por configuración")
                process_pdf_with_converter(file, output_file)
                clean_docx_styles(output_file, output_file)
            except Exception as e:
                print(f"\u274c Error al convertir {file.name}: {e}")
                process_pdf_with_ocr(file, ocr_dir)

    print("\n\u2705 Limpieza completada.")


if __name__ == "__main__":
    cfg_path = Path("config.yaml")
    cfg = safe_load(cfg_path.read_text(encoding="utf-8"))

    input_dir = Path(cfg["paths"]["originals"])
    output_dir = Path(cfg["paths"]["cleaned"])
    output_dir.mkdir(parents=True, exist_ok=True)
    batch_process_directory(input_dir, output_dir, cfg)
