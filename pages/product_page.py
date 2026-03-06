from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def should_message_be_appeared(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Секция сообщений не появилась"

    def should_not_be_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Сообщение появилось за указанное время"

    def should_message_be_dissapeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Сообщение не исчезло за указанное время"

    def should_alert_title_and_book_title_be_same(self):
        assert (
            self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
            == self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_ALERT).text
        ), "Название книги в секции сообщений не совпадает с тем, что на карточке книги"

    def should_alert_cost_and_book_cost_be_same(self):
        assert (
            self.browser.find_element(*ProductPageLocators.ALERT_COST).text
            == self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        ), "Стоимость книги в секции сообщений не совпадает с тем, что на карточке книги"
