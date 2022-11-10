from bs4 import BeautifulSoup

from attributes import Attributes


def allegro_offer(soup: BeautifulSoup):
    title = soup.find("h4").string

    price_label = soup.select_one('div[aria-label^="cena "]')["aria-label"]
    _, price, currency = price_label.split()
    price = price.replace(",", ".")

    description = soup.find("div", {"data-box-name": "Container Description card"}).text

    categories_ol = soup.find("ol", {"data-role": "breadcrumbs-list"})
    categories = [li.text for li in categories_ol.find_all("li")]

    return Attributes(
        title=title,
        price=price,
        description=description,
        categories=categories,
    )


