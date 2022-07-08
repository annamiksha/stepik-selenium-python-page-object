from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = 'accounts/login'
        current_url = self.browser.current_url
        assert login_url in current_url, 'Wrong url: not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Cannot find login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Cannot find register form'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()

    def check_no_error_message(self):
        assert self.is_not_element_present(*LoginPageLocators.MESSAGE_ERROR), 'Registration failed'
