import time
import requests
from parsel import Selector
import re
from tech_news.database import create_news

headers = {"User-Agent": "Super-agent"}


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        res = requests.get(url, headers=headers)
        time.sleep(1)
        res.raise_for_status()

    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return res.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    s = Selector(text=html_content)
    return [href for href in s.css(".entry-title a::attr(href)").getall()]


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(html_content).css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    s = Selector(text=html_content)
    d = {}
    d["url"] = s.css("link[rel='canonical']::attr(href)").get()
    d["title"] = s.css(".entry-title::text").get().strip()
    d["timestamp"] = s.css(".meta-date::text").get()
    d["writer"] = s.css(".author a::text").get()
    d["reading_time"] = int(
        re.findall(r"\d+", s.css(".meta-reading-time::text").get())[0]
    )
    d["summary"] = "".join(
        s.css("div.entry-content > p:first-of-type *::text").getall()
    ).strip()
    d["category"] = s.css(".label::text").get()
    return d


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    next_pg = "https://blog.betrybe.com/"
    news = []
    while next_pg:
        res = fetch(next_pg)
        links = scrape_updates(res)

        for link in links:
            if len(news) < amount:
                news.append(scrape_news(fetch(link)))
                next_pg = scrape_next_page_link(res)
            else:
                next_pg = None
    create_news(news)
    return news
