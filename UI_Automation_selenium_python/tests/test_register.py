from datetime import datetime
import pytest
from Pages.Account_success_page import AccountSuccessPage
from Pages.Home_page import Homepage
from Pages.Register_page import RegisterPage


@pytest.mark.usefixtures('setup_teardown')
class TestRegister:

    def test_register_with_mandatory_fields(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_register()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name_text("aa")
        register_page.enter_last_name_text("bb")
        register_page.enter_email_text(self.generate_email_with_timestamp())
        register_page.enter_telephone_text("3452341234")
        register_page.enter_password_text("12345")
        register_page.enter_confirm_password_text("12345")
        register_page.click_agree_checkbox()
        register_page.click_continue_button()
        create_msg = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.success_msg_display().text.__eq__(create_msg)

    def test_register_with_all_fields(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_register()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name_text("aa")
        register_page.enter_last_name_text("bb")
        register_page.enter_email_text(self.generate_email_with_timestamp())
        register_page.enter_telephone_text("3452341234")
        register_page.enter_password_text("12345")
        register_page.enter_confirm_password_text("12345")
        register_page.click_newsletter_yes_button()
        register_page.click_agree_checkbox()
        register_page.click_continue_button()
        create_msg = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.success_msg_display().text.__eq__(create_msg)

    def test_register_with_existing_user(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_register()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name_text("aa")
        register_page.enter_last_name_text("bb")
        register_page.enter_email_text("amotooricap1@gmail.com")
        register_page.enter_telephone_text("3452341234")
        register_page.enter_password_text("12345")
        register_page.enter_confirm_password_text("12345")
        register_page.click_newsletter_yes_button()
        register_page.click_agree_checkbox()
        register_page.click_continue_button()
        error_msg = "Warning: E-Mail Address is already registered!"
        assert register_page.existing_email_warning_msg_display().text.__contains__(error_msg)

    def test_register_without_data(self):
        home_page = Homepage(self.driver)
        home_page.click_my_account()
        home_page.click_on_register()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name_text("")
        register_page.enter_last_name_text("")
        register_page.enter_email_text("")
        register_page.enter_telephone_text("")
        register_page.enter_password_text("")
        register_page.enter_confirm_password_text("")
        register_page.click_continue_button()
        errors_msg = "Warning: You must agree to the Privacy Policy!"
        assert register_page.privacy_policy_warning_msg_display().text.__contains__(errors_msg)
        firstname_errmsg = "First Name must be between 1 and 32 characters!"
        assert register_page.first_name_warning_msg_display().text.__eq__(firstname_errmsg)
        lastname_errmsg = "Last Name must be between 1 and 32 characters!"
        assert register_page.last_name_warning_msg_display().text.__eq__(lastname_errmsg)
        email_errmsg = "E-Mail Address does not appear to be valid!"
        assert register_page.email_warning_msg_display().text.__eq__(email_errmsg)
        phone_errmsg = "Telephone must be between 3 and 32 characters!"
        assert register_page.telephone_warning_msg_display().text.__eq__(phone_errmsg)
        password_errmsg = "Password must be between 4 and 20 characters!"
        assert register_page.password_text_field_warning_msg_display().text.__eq__(password_errmsg)

    def generate_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%M_%D_%H_%M_%S")
        return "aabb"+timestamp+"@gmail.com"