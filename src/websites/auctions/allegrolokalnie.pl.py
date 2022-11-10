from bs4 import BeautifulSoup

from attributes import Attributes


def allegro_lokalnie_offer(soup: BeautifulSoup):
    title = None
    price = None
    description = None
    categories = None

    return Attributes(
        title=title,
        price=price,
        description=description,
        categories=categories,
    )


def extract_attributes(url: str, soup: BeautifulSoup):
    extractors = {
        "https://allegrolokalnie.pl/oferta/": allegro_lokalnie_offer
    }

    for extract_url in extractors.keys():
        if extract_url in url:
            return extractors[extract_url](soup)
