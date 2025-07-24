"""
Script Name: functions.py
Author: Omar Mohsen
Date: 2025-07-24
Purpose: collection of Functions used for initiation of web driver & Alerts, finding elements, Key senders, and clickers
Dependencies: selenium
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_and_launch_chrome(wait,baseurl):
    # Initialization of Chrome web driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(wait)
    # redirecting to HomePage
    driver.get(baseurl)
    return driver


def class_name_finder(driver,class_name,sent_key):

    # Finding Input field by class name
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, f"{class_name}")))
    # Sending Name of Task
    element.send_keys(sent_key)
    # Sending enter key
    element.send_keys(Keys.ENTER)


def css_selector_finder(driver, selector,sent_key):
    # Finding Input field by css selector
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{selector}")))
    # Sending Name of Task
    element.send_keys(sent_key)
    # Sending enter key
    element.send_keys(Keys.ENTER)


def accept_alert(driver):
    # initiating alert handler
    Alert(driver).accept()



def css_selector_clicker(driver,selector):
    # finding hyperlink by css selector
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,f"{selector}")))
    element.click()


def class_name_clicker(driver,selector):
    # finding hyperlink by css selector
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, f"{selector}")))
    element.click()
