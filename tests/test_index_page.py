import pytest
import pages


class TestButtons:

    def test_buttons_on_main_page(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.press_link_english_lang(page)
        join_now_button = pages.index_page.get_text_from_join_now_button(page)
        assert join_now_button.strip() == 'Join now', 'Join now button text is incorrect'

