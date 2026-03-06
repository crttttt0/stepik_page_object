import pytest

from .pages import ProductPage

LINK = (
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offerN"
)


@pytest.mark.parametrize(
    "link",
    [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(3)]
)
def test_guest_can_add_product_to_basket(browser, link):
    # link = LINK
    page = ProductPage(browser, link, 10)
    page.open()

    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_message_be_appeared()
    page.should_alert_title_and_book_title_be_same()
    page.should_alert_cost_and_book_cost_be_same()