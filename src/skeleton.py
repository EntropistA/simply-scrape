from bs4 import BeautifulSoup

from attributes import Attributes


def extractor(soup: BeautifulSoup):
    return Attributes()


def extract_attributes(url: str, soup: BeautifulSoup):
    extractors = {
        "example_url": extractor
    }

    for extract_url in extractors.keys():
        if extract_url in url:
            return extractors[extract_url](soup)
