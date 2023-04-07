#https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

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
    
def start_game():    
    quote = choice(all_quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])

    #game logic
    guess=''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Gusses remaining: {remaining_guesses}\n")

        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGT!")
            break
        
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['author_bio']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here is a hint: The author was born on {birth_date} {birth_place}.")
        elif remaining_guesses ==2:
            print(f"Here is the hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses==1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here is the hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you ran out of gusses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes','n','no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() is in ('yes','y'):
        return start_game()
        #print("Ok you play again")
    else:
        print("Ok, Bye")

start_game()
