# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
import random
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

#Trying to hide bot
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
#End of hiding Bot

driver = webdriver.Chrome(executable_path='/Users/quanahbennett/PycharmProjects/SeleniumTest/chromedriver',options=option)
url= "https://soundcloud.com/"
driver.get(url)
#time.sleep(30)

wait = WebDriverWait(driver, 30)
#link = driver.find_elements_by_link_text("Sign in")
#link[0].click()
#driver.execute_script("arguments[0].click();", link[0])


# Click on Sign-in
#wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='frontHero__signin']//button[@title='Sign in']"))).click()

#SUCCESFUL LOGIN BUTTON PUSH

please = driver.find_element_by_css_selector('button.frontHero__loginButton')
please.click()

# Switch to iframe using class-name
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"webAuthContainer__iframe")))

attempt = wait.until(EC.element_to_be_clickable((By.ID,"sign_in_up_email")))
attempt.send_keys("quanahb@yahoo.com")

# Switch to default content to interact with elements outside the iframe
#driver.switch_to.default_content()

time.sleep(2)
letsgo = wait.until(EC.element_to_be_clickable((By.ID,"sign_in_up_submit")))
letsgo.click()

time.sleep(2)
heckyeah = wait.until(EC.element_to_be_clickable((By.ID,"enter_password_field")))
heckyeah.send_keys("Octavia@5")

almost = wait.until(EC.element_to_be_clickable((By.ID,"enter_password_submit")))
almost.click()

#Test for update



breakpoint()



#time.sleep(10)

driver.quit()
