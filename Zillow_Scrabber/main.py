import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time


URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.58851138476562%2C%22east%22%3A-122.27814761523437%2C%22south%22%3A37.62262539491708%2C%22north%22%3A37.92764390882676%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

CHROME_DRIVER_PATH = os.environ.get("chrome_driver_path")
GOOGLE_DOC_URL = os.environ.get("form_link")


# Defining a class to handle Selenium operations
class invoke_selenium_driver:
    def __init__(self, driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Initializing Chrome driver with options
        self.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
        #self.maximizeWindow = self.driver.maximize_window()

    def fill_form(self):
        self.driver.get(GOOGLE_DOC_URL)  # Navigating to Google Form URL
        time.sleep(1)

        # Looping through property_list and filling the form
        for i in property_list:
            address = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
            address.send_keys(i["property_address"])
            price = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
            price.send_keys(i["property_price"])
            link = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
            Submit = self.driver.find_element(By.XPATH, "//span[text()='Submit']")
            link.send_keys(i["property_link"])
            Submit.click()
            time.sleep(0.5)
            another_response = self.driver.find_element(By.XPATH, "//a[text()='Submit another response']")
            another_response.click()
            time.sleep(1)
        print("all responses recorded.")





response = requests.get (URL, headers=header)
website_html = response.text


soup = BeautifulSoup (website_html, "lxml")
script_content_list = soup.find_all("script", attrs={"type": "application/json"})
rent_data = script_content_list[1].text.replace('<!--', "")
rent_data = script_content_list[1].text.replace("-->","")
rent_data = json.loads(rent_data)

#In case dict in json changes then write it to file for better understanding what key to use to navigate to data
#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(rent_data, f, ensure_ascii=False, indent=4)
#    print("data saved successfully")

property_data = rent_data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']

property_list = []
for i in property_data:
    property_link = i["detailUrl"]
    if not property_link.startswith("https://"):
        property_link = "https://www.zillow.com" + property_link

    property_data_dict = {"property_link": property_link}
    try:
        property_data_dict["property_price"] = i["units"][0]["price"]
    except KeyError:
        property_data_dict["property_price"] = i["price"]

    property_data_dict["property_address"] = i["address"]
    property_list.append(property_data_dict)

#print(property_list)
pp(property_list)

selenium_driver = invoke_selenium_driver(CHROME_DRIVER_PATH)
selenium_driver.fill_form()
