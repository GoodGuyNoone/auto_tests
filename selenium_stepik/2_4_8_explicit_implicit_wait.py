import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()


try:
    browser.get(link)
    # price = browser.find_element(By.ID, 'price').text
    # print(price)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()
finally:
    time.sleep(10)
    browser.quit()
