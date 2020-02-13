from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://accounts.google.com'  # URL for gmail SignIn
path_to_chromedriver = '/usr/bin/chromedriver'  #  path to chromedriver in ubuntu

def wait_and_click(browser, path):
    """
    function for click event
    """
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, path))).click()

def wait_and_send_keys(browser, path, message):
    """
    function for type event
    """
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, path))).send_keys(message)

def get_browser():
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=1200,1100')
        browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options=options)
        return browser
    except Exception as ex:
        print("Exception in getting browser function: {0}".format(ex))

def google_login(browser, mail_address, mail_password):
    """
    function for google auto login
    returns browser session id
    """
    try:
        sId = browser.session_id  # assign browser session id to a variable
        browser.get(URL)
        browser.implicitly_wait(3)
        wait_and_send_keys(browser, '//*[@id="identifierId"]', mail_address)
        wait_and_click(browser, '//*[@id="identifierNext"]')
        wait_and_send_keys(browser, '//*[@id="password"]/div[1]/div/div/input', mail_password)
        wait_and_click(browser, '//*[@id="passwordNext"]')
    except Exception as ex:
        print("Exception in google login: {0}".format(ex))

def close_browser(browser):
    try:
        browser.close()
    except Exception as ex:
        print("Exception in close browser function: {0}".format(ex))
        browser.close()