# -*- coding: utf-8 -*-
"""WebsiteQuoteScraper.ipynb
"""

!pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    authors = []

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quotes.append(text)
        authors.append(author)

    return quotes, authors

quotes, authors = scrape_quotes()

df = pd.DataFrame({
    'Quote': quotes,
    'Author': authors
})

display(df.head(10))

df.to_csv('quotes.csv', index=False)