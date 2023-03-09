from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x.text
    y = calc(x)
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()

