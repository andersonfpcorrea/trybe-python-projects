import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
