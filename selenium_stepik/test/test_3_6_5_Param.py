import os
import time
import math
import pytest


from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASS')


class TestParam:
    sites = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ]
    answer_str = ''

    @pytest.mark.parametrize('link', sites)
    def test_autorization(self, browser, link):
        browser.get(link)
        WebDriverWait(browser, 60).until(lambda x: x.find_element(By.ID, 'ember33').is_displayed())
        browser.find_element(By.ID, 'ember33').click()
        browser.find_element(By.ID, 'id_login_email').send_keys(user_name)
        browser.find_element(By.ID, 'id_login_password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn[type="submit"]').click()
        time.sleep(10)
        WebDriverWait(browser, 60).until(lambda x: x.find_element(By.CSS_SELECTOR, 'textarea').is_displayed())
        if browser.find_element(By.CSS_SELECTOR, 'textarea').get_attribute('disabled'):
            browser.find_element(By.CLASS_NAME, "again-btn.white").click()
        answer = str(math.log(int(time.time())))
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea'))).send_keys(answer)
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))).click()
        actual_result = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))).text
        # if actual_result != "Correct!":
        #     answer_str += actual_result
        assert actual_result == "Correct!", f"Message is not correct!Got instead - {actual_result}"

