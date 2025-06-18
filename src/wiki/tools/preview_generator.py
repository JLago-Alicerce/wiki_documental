import shutil
from pathlib import Path

from wiki.utils.index import render_sidebar_from_index

TEMPLATE_HTML = """<!DOCTYPE html>
<html>
<head>
  <meta charset=\"UTF-8\">
  <title>Wiki documental</title>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
</head>
<body>
  <div id=\"app\">Cargando...</div>
  <script>
    window.$docsify = {
      name: 'Wiki documental',
      loadSidebar: true,
      subMaxLevel: 2,
    }
  </script>
  <script src=\"//unpkg.com/docsify/lib/docsify.min.js\"></script>
</body>
</html>
"""


def generate_docsify_preview() -> None:
    """Genera la carpeta docs_web con archivos Markdown listos para Docsify."""
    from wiki.cli import cfg

    normalized_dir = Path(cfg["paths"]["wiki"])
    output_dir = Path("docs_web")

    print(f"\U0001f4e6 Generando vista previa Docsify en: {output_dir.resolve()}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    shutil.copytree(normalized_dir, output_dir)

    # Copiar assets de forma explícita si existen
    assets_src = normalized_dir / "assets"
    if assets_src.exists():
        dest = output_dir / "assets"
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(assets_src, dest)

    # Generar _sidebar.md desde index.yaml
    sidebar_path = output_dir / "_sidebar.md"
    render_sidebar_from_index(sidebar_path)

    # Generar index.html básico de Docsify
    (output_dir / "index.html").write_text(TEMPLATE_HTML, encoding="utf-8")

    print("\u2705 Vista previa generada. Ejecuta:")
    print(f"   cd {output_dir}")
    print("   python -m http.server")
