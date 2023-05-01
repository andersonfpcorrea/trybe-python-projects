from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
import sys

# Requisitos 11 e 12
actionTable = {
    "0": lambda: get_tech_news(
        int(input("Digite quantas notícias serão buscadas:"))
    ),
    "1": lambda: search_by_title(input("Digite o título:")),
    "2": lambda: search_by_date(input("Digite a data no formato aaaa-mm-dd:")),
    "3": lambda: search_by_category(input("Digite a categoria:")),
    "4": lambda: top_5_categories(),
    "5": lambda: print("Encerrando script\n"),
}


def analyzer_menu():
    inp = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
"""
    )
    return (
        actionTable[inp]()
        if inp in actionTable
        else sys.stderr.write("Opção inválida\n")
    )
