from bs4 import BeautifulSoup

from src.websites.auctions import allegro_pl

test_urls = [
    "https://allegro.pl/oferta/smartfon-apple-iphone-8-64-gb-szary-blokada-icloud-12769260840",
]


with open("allegro_pl.txt", encoding="utf8") as f:
    html = f.read().strip()

for url in test_urls:
    print(allegro_pl.extract_attributes(url, BeautifulSoup(html, 'html.parser')))
