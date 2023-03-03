import pytest
import pages


class TestButtons:

    def test_buttons_on_main_page(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.press_link_english_lang(page)
        join_now_button = pages.index_page.get_text_from_join_now_button(page)
        sign_in_button = pages.index_page.get_text_from_sign_in_button(page)
        header_buttons = pages.index_page.get_text_from_header_buttons(page)
        assert join_now_button.strip() == 'Join now', 'Join now button text is incorrect'
        assert sign_in_button.strip() == 'Sign in', 'Sign in button text is incorrect'
        assert 'Discover' in header_buttons, 'Discover button is incorrect'
        assert 'People' in header_buttons, 'People button is incorrect'
        assert 'Learning' in header_buttons, 'Learning button is incorrect'
        assert 'Jobs' in header_buttons, 'Jobs button is incorrect'
