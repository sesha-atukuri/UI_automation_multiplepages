from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_ID = 'input-email'
    password_ID = "input-password"
    Login_xpath = '//input[contains(@class,\'btn-primary\')]'
    invalid_credential_warning_msg_xpath = '//*[@id="account-login"]/div[1]'

    def enter_email_text(self, email_text):
        self.driver.find_element(By.ID, self.email_ID).send_keys(email_text)

    def enter_password_text(self, password_text):
        self.driver.find_element(By.ID, self.password_ID).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.Login_xpath).click()

    def invalid_login_warning(self):
        return self.driver.find_element(By.XPATH, self.invalid_credential_warning_msg_xpath)
