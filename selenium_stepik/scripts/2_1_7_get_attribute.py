import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()


try:
    browser.get(link)
    x_treasure = browser.find_element(By.ID, 'treasure')
    x = x_treasure.get_attribute('valuex')
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
