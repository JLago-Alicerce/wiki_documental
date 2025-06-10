"""CLI principal del sistema."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Herramienta para gestionar la wiki documental")
    parser.add_argument("command", help="Comando a ejecutar")
    args = parser.parse_args()

    if args.command == "procesar":
        print("Procesando nuevos documentos...")
        # Aquí se llamaría a los scripts correspondientes
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
