from .pages import MainPage
from .pages import LoginPage

# Глобавльные константы для того чтобы не дублировать ссылки
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "


def test_guest_can_go_to_login_page(browser):
    link = LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


def test_guest_should_see_login_link(browser):
    link = LINK
    page = MainPage(browser, link)

    page.open()
    page.should_be_login_link()
