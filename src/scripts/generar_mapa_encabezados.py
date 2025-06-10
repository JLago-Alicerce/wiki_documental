"""Genera un mapa de encabezados a partir de un archivo Markdown."""


def generar(path: str):
    print(f"Generando mapa de encabezados para {path}...")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        generar(sys.argv[1])
    else:
        print("Debe proporcionar el archivo Markdown")
