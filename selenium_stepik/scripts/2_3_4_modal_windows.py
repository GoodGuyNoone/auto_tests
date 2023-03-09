import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x.text
    y = calc(x)
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    button_confirm = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_confirm.click()
finally:
    time.sleep(10)
    browser.quit()
