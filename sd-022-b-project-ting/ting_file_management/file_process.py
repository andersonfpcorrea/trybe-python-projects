import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for path in instance._queue:
        if path_file in path["nome_do_arquivo"]:
            return None

    dict_path = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(dict_path)
    print(dict_path, file=sys.stdout)


def remove(instance):
    removed = instance.dequeue()
    if not removed:
        return print("Não há elementos")
    print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
