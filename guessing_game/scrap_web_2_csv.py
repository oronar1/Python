#https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

all_quotes = []
base_url="https://quotes.toscrape.com/"
url = "/page/1"

with open("qoute_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["quote","author","author_bio"])

while url:
    response = requests.get(f"{base_url}{url}")
    #print(f"Now scarping {base_url}{url}...")
    page = BeautifulSoup(response.text,"html.parser")
    quotes = page.find_all(class_="quote")
    for quote in quotes:
        quote_text = quote.find(class_="text").get_text()
        author_quote=quote.find(class_="author").get_text()
        author_bio=quote.find("a")["href"]
        
        all_quotes.append({    
            "text": quote_text, #appending a quote from site to dict
            "author": author_quote,
            "author_bio": author_bio
            csv_writer.writerow([quote_text,author_quote,author_bio])
        })
    next_btn=page.find(class_="next")
    url=next_btn.find("a")["href"] if next_btn else None    #if no next button, stop the loop
    sleep(2)
