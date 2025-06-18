from __future__ import annotations

from pathlib import Path

from yaml import safe_load

from .docx_utils import clean_docx_styles
from . import pdf_utils

# Re-export Converter for backwards compatibility with tests
Converter = pdf_utils.Converter


def process_pdf_with_converter(pdf_path: Path, output_docx_path: Path) -> None:
    """Convert a PDF to DOCX using the current ``Converter`` class."""
    pdf_utils.Converter = Converter
    pdf_utils.convert_pdf_to_docx(pdf_path, output_docx_path)


def process_pdf_with_ocr(pdf_path: Path, output_dir: Path) -> None:
    """Fallback OCR extraction wrapper."""
    pdf_utils.ocr_pdf_to_markdown(pdf_path, output_dir)


def batch_process_directory(input_dir: Path, output_dir: Path, cfg: dict | None = None) -> None:
    """Clean DOCX files and convert PDFs located in ``input_dir``."""
    print(f"\n\U0001F4C2 Procesando documentos desde: {input_dir}")

    ocr_enabled = False
    ocr_dir = output_dir.parent / "ocr_outputs"
    if cfg:
        ocr_enabled = cfg.get("options", {}).get("ocr", False)
        ocr_dir = Path(cfg["paths"].get("work", output_dir.parent)) / "ocr_outputs"

    for file in sorted(input_dir.glob("*")):
        print(f"\n\U0001F4DD {file.name}")
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
