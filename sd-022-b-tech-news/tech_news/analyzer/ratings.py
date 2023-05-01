from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    n = find_news()
    cats = [c["category"] for c in n]
    return [cat[0] for cat in Counter(sorted(cats)).most_common()[0:5]]
