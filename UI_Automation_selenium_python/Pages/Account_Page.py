from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    my_account_text_xpath = '//div[@id = \'content\']/h2[text()=\'My Account\']'

    def my_account_text_display_after_login(self):
        return self.driver.find_element(By.XPATH, self.my_account_text_xpath)
