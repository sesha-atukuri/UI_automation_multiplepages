from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_ID = 'input-firstname'
    last_name_ID = 'input-lastname'
    email_ID = 'input-email'
    telephone_ID = 'input-telephone'
    password_ID = 'input-password'
    pass_confirm_ID = 'input-confirm'
    agree_checkbox_NAME = 'agree'
    continue_button_XPATH = '//input[@value=\'Continue\']'
    newsletter_yes_radio_XPATH = '//input[@name = \'newsletter\'][@ value = \'1\']'
    existing_email_address_warning_msg_XPATH = '//div[@id=\'account-register\']/div[1]'
    privacy_policy_err_msg_XPATH = '//div[@id=\'account-register\']/div[1]'
    first_name_err_msg_xpath = '//input[@id="input-firstname"]/following-sibling::div'
    last_name_err_msg_xpath = '//input[@id="input-lastname"]/following-sibling::div'
    email_err_msg_XPATH = '//input[@id="input-email"]/following-sibling::div'
    telephone_err_msg_XPATH = '//input[@id="input-telephone"]/following-sibling::div'
    password_text_field_err_msg_XPATH = '//input[@id="input-password"]/following-sibling::div'

    def enter_first_name_text(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_ID).send_keys(first_name_text)

    def enter_last_name_text(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_ID).send_keys(last_name_text)

    def enter_email_text(self, email_text):
        self.driver.find_element(By.ID, self.email_ID).send_keys(email_text)

    def enter_telephone_text(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_ID).send_keys(telephone_text)

    def enter_password_text(self, password_text):
        self.driver.find_element(By.ID, self.password_ID).send_keys(password_text)

    def enter_confirm_password_text(self, confirm_password_text):
        self.driver.find_element(By.ID, self.pass_confirm_ID).send_keys(confirm_password_text)

    def click_agree_checkbox(self):
        self.driver.find_element(By.NAME, self.agree_checkbox_NAME).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_XPATH).click()

    def click_newsletter_yes_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_yes_radio_XPATH).click()

    def existing_email_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.existing_email_address_warning_msg_XPATH)

    def privacy_policy_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_err_msg_XPATH)

    def first_name_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.first_name_err_msg_xpath)

    def last_name_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.last_name_err_msg_xpath)

    def email_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.email_err_msg_XPATH)

    def telephone_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.telephone_err_msg_XPATH)

    def password_text_field_warning_msg_display(self):
        return self.driver.find_element(By.XPATH, self.password_text_field_err_msg_XPATH)
