"""Normaliza los estilos de documentos DOCX."""


def normalizar(path: str):
    print(f"Normalizando estilos en {path}...")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        normalizar(sys.argv[1])
    else:
        print("Debe proporcionar el archivo a normalizar")
