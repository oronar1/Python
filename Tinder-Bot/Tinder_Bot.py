from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = '*****'
ACCOUNT_PASSWORD = '****'

# Optional - Keep the browser open if the script crashes.
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://tinder.com/")

# Accept Cookies
original_window = driver.current_window_handle

accept_cookies = driver.find_element(By.XPATH,value='//*[@id="c619680161"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Log in").click()

time.sleep(5)

driver.find_element(By.TAG_NAME, "iframe").click()

g_login=driver.window_handles[1]
driver.switch_to.window(g_login)
time.sleep(3)
driver.find_element(By.TAG_NAME, "input").send_keys(ACCOUNT_EMAIL)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(2)

print(driver.title)


driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(ACCOUNT_PASSWORD, Keys.ENTER)
time.sleep(2)
print(driver.title)

driver.switch_to.window(original_window)

# Allow location
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="c-1108700915"]/main/div/div/div/div[3]/button[1]/div[2]').click()

#Don't allow notifications
driver.find_element(By.XPATH, '//*[@id="c-1108700915"]/main/div[1]/div/div/div[3]/button[2]/div[2]').click()
time.sleep(5)

for n in range(20):
    #driver.find_element(By.XPATH,'//*[@id="c619680161"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button/span/span/svg/path')\.click()
    time.sleep(2)
    try:
        print("right swipe")
        #driver.find_element(By.TAG_NAME,value='body').send_keys((Keys.ARROW_RIGHT))
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
    #catches "Matched" Pop up pwindow on top of like button
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
    #driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_LEFT)
    time.sleep(10)
