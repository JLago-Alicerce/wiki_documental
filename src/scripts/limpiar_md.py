"""Limpieza básica de archivos Markdown."""


def limpiar(path: str):
    print(f"Limpiando el archivo Markdown {path}...")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        limpiar(sys.argv[1])
    else:
        print("Debe proporcionar el archivo Markdown a limpiar")
