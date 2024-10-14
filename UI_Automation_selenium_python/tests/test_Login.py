from datetime import datetime
import pytest
from Pages.Account_Page import AccountPage
from Pages.Home_page import Homepage
from Pages.Login_Page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
class TestLogin:

    def test_login_invalid_credentials(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_login()
        login_page = LoginPage(self.driver)
        login_page.enter_email_text(self.generate_email_with_timestamp())
        login_page.enter_password_text("12345")
        login_page.click_on_login_button()
        warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.invalid_login_warning().text.__contains__(warning_message)

    def test_login_valid_credentials(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_login()
        login_page = LoginPage(self.driver)
        login_page.enter_email_text('amotooricap1@gmail.com')
        login_page.enter_password_text("12345")
        login_page.click_on_login_button()
        account_page = AccountPage(self.driver)
        assert account_page.my_account_text_display_after_login()

    def test_login_valid_user_invalid_pass(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_login()
        login_page = LoginPage(self.driver)
        login_page.enter_email_text('amotooricap1@gmail.com')
        login_page.enter_password_text("acvbg")
        login_page.click_on_login_button()
        warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.invalid_login_warning().text.__contains__(warning_message)

    def test_login_invaliduser_validpass(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_login()
        login_page = LoginPage(self.driver)
        login_page.enter_email_text(self.generate_email_with_timestamp())
        login_page.enter_password_text("12345")
        login_page.click_on_login_button()
        warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.invalid_login_warning().text.__contains__(warning_message)

    def generate_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%M_%D_%H_%M_%S")
        return "aabb"+timestamp+"@gmail.com"
