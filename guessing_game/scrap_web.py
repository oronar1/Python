#https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

all_quotes = []
base_url="https://quotes.toscrape.com/"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    #print(f"Now scarping {base_url}{url}...")
    page = BeautifulSoup(response.text,"html.parser")
    quotes = page.find_all(class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(), #appending a quote from site to dict
            "author": quote.find(class_="author").get_text(),
            "author_bio": quote.find("a")["href"]
        })
    next_btn=page.find(class_="next")
    url=next_btn.find("a")["href"] if next_btn else None    #if no next button, stop the loop
    sleep(2)
