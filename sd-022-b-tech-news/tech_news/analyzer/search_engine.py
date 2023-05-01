from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    q = {"title": {"$regex": f"{title}", "$options": "-i"}}
    results = search_news(q)
    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        d = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news_list = search_news({"timestamp": d})
        return [(n["title"], n["url"]) for n in news_list]
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    q = search_news({"category": {"$regex": category, "$options": "-i"}})
    return [(news["title"], news["url"]) for news in q]
