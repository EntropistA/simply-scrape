from bs4 import BeautifulSoup

from src.simply_scrape.websites.auctions import allegro
from src.simply_scrape.websites.auctions.attributes import OfferAttributes

def read_soup_from_file(filename: str):
    with open(filename, encoding="utf8") as f:
        html = f.read().strip()
    return BeautifulSoup(html, 'html.parser')


test_urls_soups = {
    "https://allegro.pl/oferta/smartfon-apple-iphone-8-64-gb-szary-blokada-icloud-12769260840": read_soup_from_file("test1.txt"),
}


for url, soup in test_urls_soups.items():
    print(allegro.extract_attributes(url, soup))
