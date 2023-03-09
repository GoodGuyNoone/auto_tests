from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class test_1_6_11(unittest.TestCase):
    def test_1_6_11_link1(self):
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        first_name.send_keys("name")
        last_name.send_keys("last name")
        email.send_keys("email")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'welcome_text is not correct')

    def test_1_6_11_link2(self):
        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        first_name.send_keys("name")
        last_name.send_keys("last name")
        email.send_keys("email")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'welcome_text is not correct')


if __name__ == "__main__":
    unittest.main()
