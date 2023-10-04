import os
import pickle
from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

APP_ID = os.environ["APP_ID"]
COOKIES_FILE = 'cookies.pkl'
INSTAGRAM_URL = 'https://www.instagram.com/accounts/login/'
IG_URL='https://www.instagram.com/'
INSTAGRAM_EMAIL = os.environ["INSTA_MAIL"]
INSTAGRAM_PASSWORD = os.environ["INSTA_PASSWORD"]
INSTAGRAM_USER = os.environ["INSTA_USER"]
IG_TARGET = 'insta_target'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    """A class for following Instagram followers from selected account."""
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(self.options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(INSTAGRAM_URL)
        #self.driver.maximize_window()


    def login(self):
        # Loading cookies if they exist
        if os.path.exists(COOKIES_FILE):
            print("Started login in")
            with open(COOKIES_FILE, 'rb') as file:
                file_path = os.path.abspath(COOKIES_FILE)
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                 #   print(cookie)
            self.driver.refresh()


        try:
            sleep(5)
            username_field = self.driver.find_element(By.NAME, "username")
            username_field.send_keys(INSTAGRAM_EMAIL)
            password_field = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
            password_field.send_keys(INSTAGRAM_PASSWORD)
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
            sleep(6)

            # Save the updated cookies
            cookies = self.driver.get_cookies()
            with open(COOKIES_FILE, 'wb') as file:
                pickle.dump(cookies, file)

            now_button = self.driver.switch_to.active_element
            now_button.send_keys(Keys.TAB)
            not_now_button = self.driver.switch_to.active_element
            not_now_button.click()
            sleep(5)
            self.driver.switch_to.active_element.send_keys(Keys.TAB)
            not_now_button1 = self.driver.switch_to.active_element
            not_now_button1.click()
            sleep(5)

        except:
            sleep(10)
        else:
            pass

    def find_followers(self):
        self.driver.get(IG_URL + '/' + IG_TARGET + '/following')
        sleep(3)
        elem = self.driver.switch_to.active_element
        elem.send_keys(Keys.TAB)
        i = 0
        Keep_Adding = True
        while Keep_Adding:
            sleep(1)
            elem = self.driver.switch_to.active_element
            try:
                if elem.text == 'Follow':
                    elem.click()
                    i = i + 1       
                    #print("Clicking on Follow")
                elem.send_keys(Keys.TAB)
            except ElementNotInteractableException:
                continue
            #If following that user already
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
            if i > 200:
              print("Added 200 Followers to account")
              Keep_Adding = False
              print("Exiting)"
              sleep(2)
            #not needed cause using TAB insted.
            #scrolling the window of followers
            #modal = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]')
            #for i in range(10):
                # In this case we're executing some Javascript, that's what the execute_script() method does.
                # The method can accept the script as well as a HTML element.
                # The modal in this case, becomes the arguments[0] in the script.
                # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            #    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            #    sleep(2)

                    
    def follow(self):
        """Function to add All followers of the requiered account"""      
        sleep(5)

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")

        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()




insta_followers_bot = InstaFollower()
insta_followers_bot.login()
insta_followers_bot.find_followers()
