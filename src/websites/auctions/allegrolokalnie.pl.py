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

