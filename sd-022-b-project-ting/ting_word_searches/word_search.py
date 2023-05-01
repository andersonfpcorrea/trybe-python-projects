from ting_file_management.queue import Queue


def exists_word(word, instance: Queue, src_by_word=False):
    res = []
    src_i = 0

    while len(res) == 0 and src_i < instance.__len__():
        item = instance.search(src_i)
        occrs = []

        for index, line in enumerate(item["linhas_do_arquivo"]):
            occr = (
                {"linha": index + 1, "conteudo": line}
                if src_by_word
                else {"linha": index + 1}
            )
            if word.lower() in line.lower():
                occrs.append(occr)

        result = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": occrs,
        }

        if len(result["ocorrencias"]) > 0:
            res.append(result)

        src_i += 1

    return res


def search_by_word(word, instance):
    return exists_word(word, instance, src_by_word=True)
