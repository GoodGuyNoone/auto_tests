import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()


try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x.text
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_field.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
