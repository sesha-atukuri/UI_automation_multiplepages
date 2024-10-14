from selenium.webdriver.common.by import By


class AccountSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    new_account_success_msg_XPATH = '//div[@id=\'content\']/h1'

    def success_msg_display(self):
        return self.driver.find_element(By.XPATH, self.new_account_success_msg_XPATH)