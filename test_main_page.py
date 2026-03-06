# Тесты для проверки авторизации на главной странице
import time

import pytest

from .pages import LoginPage, MainPage

# Глобальная константа URL, чтобы не повторять строку несколько раз
LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link)

        page.open()
        # Переходим на страницу логина
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()

    def test_guest_should_see_login_link(self, browser):
        link = LINK
        page = MainPage(browser, link)

        page.open()
        # На главной должна быть ссылка на страницу входа
        page.should_be_login_link()
