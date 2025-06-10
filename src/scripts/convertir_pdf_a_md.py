"""Convierte archivos PDF a Markdown."""


def convertir(path: str):
    print(f"Convirtiendo {path} a Markdown...")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        convertir(sys.argv[1])
    else:
        print("Debe proporcionar el PDF a convertir")
