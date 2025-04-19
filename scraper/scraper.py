import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_books(html):
    soup = BeautifulSoup(html, 'html.parser')
    books = []

    for article in soup.select('article.product_pod'):
        title = article.h3.a['title']
        price = article.select_one('p.price_color').text.strip()
        link = urljoin(BASE_URL, article.h3.a['href'])
        rating_class = article.select_one('p.star-rating')['class'][1]  # e.g., "Three"

        books.append({
            "title": title,
            "price": price,
            "url": link,
            "rating": rating_class
        })

    return books

def get_all_books():
    books = []
    next_page = "catalogue/page-1.html"

    while next_page:
        logging.info(f"Fetching page: {next_page}")
        html = fetch_page(urljoin(BASE_URL, next_page))
        books.extend(parse_books(html))

        soup = BeautifulSoup(html, 'html.parser')
        next_btn = soup.select_one('li.next a')
        next_page = urljoin("catalogue/", next_btn['href']) if next_btn else None

    return books
