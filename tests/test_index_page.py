import pytest
import pages


class TestFooter:

    def test_main_buttons_on_main_page(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.press_link_english_lang(page)
        actual_result = pages.index_page.get_text_from_join_now_button(page)
        assert actual_result.strip() == 'Join now', 'Join now button text is incorrect'
