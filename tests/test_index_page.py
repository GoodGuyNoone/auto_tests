import pytest
import pages
import time


class TestFooter:

    def test_main_buttons_on_main_page(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(10)