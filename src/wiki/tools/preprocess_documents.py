from pathlib import Path
import docx
from docx.document import Document
from docx.text.paragraph import Paragraph
from pdf2docx import Converter
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


def batch_process_directory(input_dir: Path, output_dir: Path):
    print(f"\n\U0001f4c2 Procesando documentos desde: {input_dir}")
    for file in sorted(input_dir.glob("*")):
        print(f"\n\U0001f4dd {file.name}")
        output_file = output_dir / (file.stem + ".docx")

        if file.suffix.lower() == ".docx":
            clean_docx_styles(file, output_file)

        elif file.suffix.lower() == ".pdf":
            try:
                print("   → Convirtiendo PDF a DOCX...")
                converter = Converter(str(file))
                converter.convert(str(output_file), start=0, end=None)
                converter.close()
                clean_docx_styles(output_file, output_file)
            except Exception as e:
                print(f"\u274c Error al convertir {file.name}: {e}")

    print("\n\u2705 Limpieza completada.")


if __name__ == "__main__":
    cfg_path = Path("config.yaml")
    cfg = safe_load(cfg_path.read_text(encoding="utf-8"))

    input_dir = Path(cfg["paths"]["cleaned_input"])
    output_dir = Path(cfg["paths"]["cleaned_output"])
    output_dir.mkdir(parents=True, exist_ok=True)
    batch_process_directory(input_dir, output_dir)
