from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET)

    def should_be_text_about_empty_basket(self):
        empty_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert (
            "Your basket is empty" in empty_text.text
        ), f"Неправилая информация о наполнении корзины: {empty_text.text}"
