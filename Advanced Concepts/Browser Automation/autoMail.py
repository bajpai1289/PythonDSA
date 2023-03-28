from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
# import org.openqa.selenium.support.ui.Select
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
browser.get("https://www.google.com/gmail/about/")
signIn = browser.find_element(By.LINK_TEXT,"Sign in")
signIn.click()
sleep(0.5)
email = browser.find_element(By.ID, "identifierId")
email.send_keys("abhishek.bajpai@velocitai.com")
sleep(1)
s1 = browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)")
s1.click()
sleep(2)
passw = browser.find_element(By.CSS_SELECTOR, "#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
passw.send_keys("Home@1289")
sleep(1)
s1 = browser.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)")
s1.click()
sleep(3)

compose = browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(19) > div.nH > div > div.nH.aqk.aql.bkL > div.aqn.aIH.nH.oy8Mbf.apV > div.aBO > div.aic > div > div")
x=input()