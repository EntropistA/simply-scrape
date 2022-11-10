# simply-scrape

## Purpose

The goal is to get attributes from already obtained
BeautifulSoup object containing request's result as a text.


## Project Structure
```
simply_scrape
│
└───auctions
│   │   amazon.py
│   │   allegro.py
│   │   allegrolokalnie.py
│   
└───news
│   │   nytimes.py
│   │   theguardian.py

```


## Usage
```python
from simply_scrape.websites.auctions import allegro_pl
attributes = allegro_pl.allegro_offer(soup)
print(attributes)

# Result:
Attributes(title='Smartfon Apple iPhone 8 2 GB / 64 GB szary', price='299.00')
```


## Notes

Implementation of getting website in a text structure **is not** implemented.

This can be done using **requests** or **selenium** modules.

```python
import requests
from bs4 import BeautifulSoup
html_doc = requests.get("google.com").text
soup = BeautifulSoup(html_doc, 'html.parser')
```



