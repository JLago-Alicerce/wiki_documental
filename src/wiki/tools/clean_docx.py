from pathlib import Path

from .docx_utils import clean_docx_styles


def batch_process_directory(input_dir: Path, output_dir: Path):
    print(f"\n\U0001f4c2 Procesando .docx desde: {input_dir}")
    for docx_file in sorted(input_dir.glob("*.docx")):
        print(f"\n\U0001f4dd {docx_file.name}")
        output_file = output_dir / docx_file.name
        clean_docx_styles(docx_file, output_file)

    print("\n\u2705 Limpieza completada.")

