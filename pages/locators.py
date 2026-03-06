from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_SECTION = (By.ID, "messages")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_TITLE_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_COST = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
