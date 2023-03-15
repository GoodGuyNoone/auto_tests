import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_item_button_is_presented(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket") is not None,\
        'There is no Add to basket button'
