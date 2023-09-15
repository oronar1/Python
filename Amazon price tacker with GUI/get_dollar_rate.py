import requests
from bs4 import BeautifulSoup


dollar_rate = float(BeautifulSoup(requests.get("https://www.forbes.com/advisor/money-transfer/currency-converter/usd-pkr/").text,
                                  'html.parser').select_one('.amount').text)