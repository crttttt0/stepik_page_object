from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")

    VIEW_CART = (By.CSS_SELECTOR, ".btn-group > a")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_RETYPE = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_SECTION = (By.CLASS_NAME, "alert-success")

    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_TITLE_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    BOOK_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_COST = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")


class BasketPageLocators:
    BASKET = (By.CLASS_NAME, "basket-title")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
