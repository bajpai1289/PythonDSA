from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from passwords import VelocitaiPassword, VelocitaiUsername

browser = webdriver.Chrome()
browser.get("https://velocitai.greythr.com/uas/portal/auth/login")
sleep(0.5)
userName = browser.find_element(By.ID,"username")
userName.send_keys(VelocitaiUsername)
password = browser.find_element(By.ID, "password")
password.send_keys(VelocitaiPassword)
password.submit()
sleep(4)
btn = browser.find_element(By.CSS_SELECTOR,".btn-container > .hydrated")
btn.click()
sleep(1)
# x=input()