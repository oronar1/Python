from tkinter import messagebox
from send_mail import internet
import json
from bs4 import BeautifulSoup
import requests

# Amazon Header
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def create_soup(url):
    return BeautifulSoup(requests.get(url, headers=header).text, 'html.parser')

def check_valid_url(url):
    soup = create_soup(url)
    return False if "Page Not Found" in soup.text else soup


def uploading_data_to_json_file(url, price):
    try:
        with open("url_info.json", "r+") as file:
            file_data = json.load(file)
            for u in file_data:
                if file_data[u]['url'] == url:
                    return False
            file_data[f"URL{len(file_data) + 1}"] = {"url": url, "myBudget": float(price)}
            file.seek(0)
            json.dump(file_data, file, indent=4)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("url_info.json", "w") as file:
            new_data = {"URL1": {"url": url, "myBudget": float(price)}}
            json.dump(new_data, file, indent=4)

def add_url(url, price):
    # validation url and price
    if not url or not price:
        return messagebox.showerror(title="Invalid Fields", message="Please Complete all the fields!")
    if not internet():
        return messagebox.showerror("No internet Connection", message="Please check your internet!!")
    if url[:23] != "https://www.amazon.com/":
        return messagebox.showerror(title="ONLY AMAZON URL", message="Please enter only url from amazon website!!")
    try:
        float(price)
    except ValueError:
        return messagebox.showerror(title="Price Issue", message="Enter Price something like 20.35, 12, 191.2 etc!!")

    soup = check_valid_url(url)
    if not soup:
        return messagebox.showerror("Invalid Url", message="We could not find the page with that url")
    if uploading_data_to_json_file(url, price) is False:
        return messagebox.showerror(title="URL Already Exists", message="This Url Already Exists Please Change the url")
    messagebox.showinfo(title="URL ADDED", message=f"URL with ${price} has been added successfully!!")
    return True
