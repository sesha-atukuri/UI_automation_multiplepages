from selenium.webdriver.common.by import By
from selenium.webdriver.support.page_factory import PageFactory

class Homepage:

    def __init__(self,driver):
        self.driver = driver

    search_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_xpath = "//span[text()='My Account']"
    login_link_text = "Login"
    home_register_link_text = 'Register'

    def enter_product_name(self, product_name):
        self.driver.find_element(By.NAME, self.search_field_name).click()
        self.driver.find_element(By.NAME, self.search_field_name).clear()
        self.driver.find_element(By.NAME, self.search_field_name).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()

    def click_on_register(self):
        self.driver.find_element(By.LINK_TEXT, self.home_register_link_text).click()
