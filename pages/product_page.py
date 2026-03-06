from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Страница товара и действия, доступные на ней"""

    def add_to_cart(self):
        # Клик по кнопке "Добавить в корзину"
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def should_message_be_appeared(self):
        # Проверяем, что появилась секция с сообщением об успехе
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Секция сообщений не появилась"

    def should_not_be_message(self):
        # Убеждаемся, что сообщение не появилось в течение таймаута
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Сообщение появилось за указанное время"

    def should_message_be_dissapeared(self):
        # Проверяем, что сообщение исчезло через некоторое время
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_SECTION
        ), "Сообщение не исчезло за указанное время"

    def should_alert_title_and_book_title_be_same(self):
        # Сравниваем название товара в карточке и в сообщении об добавлении
        assert (
            self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
            == self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_ALERT).text
        ), "Название книги в секции сообщений не совпадает с тем, что на карточке книги"

    def should_alert_cost_and_book_cost_be_same(self):
        # Сравниваем цену товара в карточке и в сообщении об добавлении
        assert (
            self.browser.find_element(*ProductPageLocators.ALERT_COST).text
            == self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        ), "Стоимость книги в секции сообщений не совпадает с тем, что на карточке книги"
