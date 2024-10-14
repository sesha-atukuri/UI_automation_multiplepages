from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self,driver):
        self.driver = driver

    product_search_link_text = "HP LP3065"
    no_product_warning_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def product_text_display(self):
        return self.driver.find_element(By.LINK_TEXT, self.product_search_link_text).is_displayed()

    def product_warning_message(self):
        return self.driver.find_element(By.XPATH, self.no_product_warning_message_xpath).text

