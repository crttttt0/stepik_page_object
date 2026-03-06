import pytest, time

from .pages import ProductPage, BasketPage, LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    
    page = ProductPage(browser, link, 10)
    page.open()

    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_message_be_appeared()
    page.should_alert_title_and_book_title_be_same()
    page.should_alert_cost_and_book_cost_be_same()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_to_cart()
    page.should_not_be_message()
    
    
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        
        page.register_new_user(str(time.time()) + "@fakemail.org", "qwertyyyy")
        page.should_be_authorized_user()
    
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()

        page.add_to_cart()
        page.solve_quiz_and_get_code()

        page.should_message_be_appeared()
        page.should_alert_title_and_book_title_be_same()
        page.should_alert_cost_and_book_cost_be_same()


    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()

        page.add_to_cart()
        page.should_not_be_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_to_cart()
    page.should_message_be_dissapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()

    page.go_to_cart()
    page.should_not_be_products_in_basket()
    page.should_be_text_about_empty_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()

    page.go_to_cart()
    page.should_not_be_products_in_basket()
    page.should_be_text_about_empty_basket()
