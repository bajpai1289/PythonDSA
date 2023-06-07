from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from passwords import VelocitaiPassword, VelocitaiUsername
import datetime

def is_weekend_morning():
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().weekday()

    is_weekend = current_day == 5 or current_day == 6
    is_morning = datetime.time(8, 0) <= current_time <= datetime.time(11, 0)

    return is_weekend or not is_morning
if is_weekend_morning():
    exit(0)

browser = webdriver.Chrome()
browser.get("https://velocitai.greythr.com/uas/portal/auth/login")
sleep(1)
userName = browser.find_element(By.ID,"username")
userName.send_keys(VelocitaiUsername)
password = browser.find_element(By.ID, "password")
password.send_keys(VelocitaiPassword)
password.submit()
sleep(7)
btn = browser.find_element(By.CSS_SELECTOR,".btn-container > .hydrated")
btn.click()
sleep(1)
# x=input()
