from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link2)
    first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    first_name.send_keys("name")
    last_name.send_keys("last name")
    email.send_keys("email")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
