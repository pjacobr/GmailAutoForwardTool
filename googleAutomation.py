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
