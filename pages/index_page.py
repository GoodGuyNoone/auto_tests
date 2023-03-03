from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_JOIN_NOW = "//html/body/nav/div/a[1]"
    _BUTTON_SIGN_IN = "//html/body/nav/div/a[2]"
    _BUTTON_DISCOVER = "//html/body/nav/ul/li[1]/a/span"
    _BUTTON_PEOPLE = '//html/body/nav/ul/li[2]/a/span'
    _BUTTON_LEARNING = '//html/body/nav/ul/li[3]/a/span'
    _BUTTON_JOBS = '//html/body/nav/ul/li[4]/a/span'
    _LINK_LANGUAGES = "//html/body/footer/ul/li[11]/div/button"
    _LINK_LANGUAGE_ENG = "//html/body/footer/ul/li[11]/div/ul/li[5]/button"


    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.MAIN_PAGE)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_LANGUAGES).click()
        page.locator(self._LINK_LANGUAGE_ENG).click()

    def get_text_from_join_now_button(self, page: Page) -> str:
        return page.locator(self._BUTTON_JOIN_NOW).inner_text()

    def get_text_from_sign_in_button(self, page: Page) -> str:
        return page.locator(self._BUTTON_SIGN_IN).inner_text()

    def get_text_from_header_buttons(self, page: Page) -> list:
        header_buttons = [
                          page.locator(self._BUTTON_DISCOVER).inner_text(),
                          page.locator(self._BUTTON_PEOPLE).inner_text(),
                          page.locator(self._BUTTON_LEARNING).inner_text(),
                          page.locator(self._BUTTON_JOBS).inner_text()
                          ]
        return header_buttons

