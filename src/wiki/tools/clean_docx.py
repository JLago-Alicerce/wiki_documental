from pathlib import Path
import docx
from docx.document import Document
from docx.text.paragraph import Paragraph

# Configuración de heurísticas
HEADING_1_MIN_FONT_SIZE = 14  # pt
HEADING_2_MIN_FONT_SIZE = 12


def is_likely_heading(p: Paragraph) -> int:
    if not p.text.strip():
        return 0
    bold_runs = [r.bold for r in p.runs if r.text.strip()]
    if not bold_runs or not all(bold_runs):
        return 0
    if p.style.name.startswith('List'):
        return 0
    if len(p.text.strip().split()) > 10:
        return 0
    for r in p.runs:
        if r.text.strip() and r.font.size:
            first_run_size = r.font.size.pt
            if first_run_size >= HEADING_1_MIN_FONT_SIZE:
                return 1
            if first_run_size >= HEADING_2_MIN_FONT_SIZE:
                return 2
    return 0


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
            print(f"  -> '{p.text[:50].strip()}' \u2192 Heading {heading_level}")
            p.style = f'Heading {heading_level}'
            changes_made = True

    if changes_made:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output_path)
        print(f"\u2705 Guardado: {output_path.name}")

    return changes_made


def batch_process_directory(input_dir: Path, output_dir: Path):
    print(f"\n\U0001f4c2 Procesando .docx desde: {input_dir}")
    for docx_file in sorted(input_dir.glob("*.docx")):
        print(f"\n\U0001f4dd {docx_file.name}")
        output_file = output_dir / docx_file.name
        clean_docx_styles(docx_file, output_file)

    print("\n\u2705 Limpieza completada.")

