from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Ссылка не принадлежит странице авторизации/входа"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        )
        password_retype_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_RETYPE
        )
        registration_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON
        )

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_retype_input.send_keys(password)
        registration_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *LoginPageLocators.USER_ICON
        ), "Не найдена иконка пользователя. Скорее всего, он не авторизован"
