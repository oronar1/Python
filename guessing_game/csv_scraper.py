#https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from csv import Dictwriter
from time import sleep
from random import choice


BASE_URL="https://quotes.toscrape.com/"


def scrape_quotes():
    all_quotes = []
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
        sleep(1)
    return all_quotes

#write to csv file
def write_quotes(quotes):
    with open("quotes.csv","w") as file:
        headers = ["text","author","bio_link"]
        csv_writer = Dictwriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)
            
quotes = scrape_quotes()
write_quotes(quotes)