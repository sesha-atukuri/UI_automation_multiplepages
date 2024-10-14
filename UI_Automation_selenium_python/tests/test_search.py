import pytest
from selenium.webdriver.common.by import By

from Pages.Home_page import Homepage
from Pages.Search_page import SearchPage


@pytest.mark.usefixtures("setup_teardown")
class TestSearch:

    def test_search_for_a_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_name("HP")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.product_text_display()

    def test_search_for_invalid_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_name("Honda")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.product_warning_message()

    def test_search_for_no_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_name("")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.product_warning_message()





