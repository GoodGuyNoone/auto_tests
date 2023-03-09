import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, '.form-group > input[name="firstname"]')
    last_name = browser.find_element(By.CSS_SELECTOR, '.form-group > input[name="lastname"]')
    email = browser.find_element(By.CSS_SELECTOR, '.form-group > input[name="email"]')
    file_button = browser.find_element(By.ID, 'file')
    first_name.send_keys('first name')
    last_name.send_keys('last name')
    email.send_keys('email@email.com')
    file_button.send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()
