from add_url_to_file import create_soup
from send_mail import internet
from tkinter import messagebox
from get_dollar_rate import dollar_rate
import json

d_rate = 0
message_to_send = ""

# check product available or not
def product_availability(sp):
    try:
        available_info = sp.select_one("#availability").text.strip()
    except AttributeError:
        return True
    else:
        return False if not available_info or "Currently unavailable." in available_info else True

def get_product_price(soup):
    try:
        return float("".join(soup.find (name="span", class_="a-offscreen").getText().split("$")[1]))
    except ValueError:
        return float(soup.find (name="span", class_="a-offscreen").getText().split("$")[1])
    except AttributeError:
        return None

def cheap_product_info(soup, low_price, url):
    global message_to_send
    price = get_product_price(soup)
    print(price)
    if price < low_price:
        product_title = soup.find(id="productTitle").text.strip()
        rating = soup.select_one('.a-icon-alt').text.split()[0]
        message_to_send += f"PRODUCT: {product_title}\nPrice: ${price} ({round(price * d_rate, 2)}PKR)\nRating: {rating}/5\n{url}\n\n\n"

def track_prices():
    global d_rate
    if not internet():
        return messagebox.showerror("No internet Connection", message="Please check your internet!!")
    d_rate = dollar_rate
    try:
        with open("url_info.json") as file:
            file_data = json.load(file)
            for url in file_data:
                print(url)
                soup = create_soup(file_data[url]['url'])
                if product_availability(soup):
                    cheap_product_info(soup, file_data[url]['myBudget'], file_data[url]['url'])
            return message_to_send
    except FileNotFoundError:
        messagebox.showerror("FILE NOT FOUND", message="File \"url_info.json\" not found!")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("EMPTY FILE", message="File \"url_info.json\" is empty!!")
