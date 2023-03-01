from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_JOIN_NOW = "//html/body/nav/div/a[1]"
    _LINK_LANGUAGES = "//html/body/footer/ul/li[11]/div/button"
    _LINK_LANGUAGE_ENG = "//html/body/footer/ul/li[11]/div/ul/li[5]/button"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_LANGUAGES).click()
        page.locator(self._LINK_LANGUAGE_ENG).click()

    def get_text_from_join_now_button(self, page: Page) -> str:
        return page.locator(self._BUTTON_JOIN_NOW).inner_text()
