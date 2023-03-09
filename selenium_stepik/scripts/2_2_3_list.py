from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    sum_num = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum_num))
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(10)
    browser.quit()

