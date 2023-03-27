from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# import org.openqa.selenium.support.ui.Select
from selenium.webdriver.support.ui import Select
while True:
    browser = webdriver.Chrome()
    browser.get("https://velocitai.com/career")
    head=browser.find_element(By.CLASS_NAME, 'widget-wrap-children')
    head.click()
    sleep(4)
    
    body = browser.find_element(By.LINK_TEXT,"Mail Your CV")
    body.click()
    sleep(0.6)
    name = browser.find_element(By.ID, "form-field-your_name")
    mail = browser.find_element(By.ID, "form-field-your_email")
    num= browser.find_element(By.ID, "form-field-mobile_number")
    select = Select(browser.find_element(By.ID, "form-field-degree"))
    select.select_by_visible_text('Doctoral Degree')

    cv = browser.find_element(By.ID, "form-field-cv_upload")
    name.send_keys("Shiana")
    mail.send_keys("shiana.soni@velocitai.com")
    num.send_keys("3216549870")
    cv.send_keys(r"C:\Users\abhis\OneDrive\Documents\PythonDSA\rotated.pdf")


    # send = browser.find_element(By.LINK_TEXT, "")
    send = browser.find_element(By.CSS_SELECTOR,"button.elementor-button")
    send.click()
    sleep(5)
    browser.close()
# x=input()

# name = browser.find_element(By.ID, "form-field-your_name")
# name.send_keys("Tanya")

# fontsUsed = []
# fonts = {"Roboto", "arial", "roboto", "Arial"}
# for text in browser.page_source:
#     if text in fonts:
#         fontsUsed.append(text)

# print(fontsUsed)

# sleep(10)


# signinLink.click()
# sleep(1)

# usernameBox= browser.find_element(By.ID,"login_field")
# usernameBox.send_keys("Abhishek-Baj1289")
# passwordBox = browser.find_element(By.ID, "password")
# passwordBox.send_keys("Velocitai@123")
# passwordBox.submit()

# sleep(0.5)
# assert "Abhishek-Baj1289" in browser.page_source
# test = (browser.page_source)
# with open('pageSource.txt','w',encoding='utf-8') as file:
    # file.write(test)
# profileLink =browser.find_element(By.CLASS_NAME,"user-profile-link")
# linkLabel=profileLink.get_attribute("innerHTML")
# assert "Abhishek-Baj12389" in linkLabel
    
# x=input()
