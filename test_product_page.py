import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link_list =  [
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.need_review
@pytest.mark.parametrize('link', link_list)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_product_added_to_cart_message()
    page.check_product_name_added_to_cart()
    page.check_price_added_to_cart()
    

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_cart()
    page.success_message_must_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, )
    page.open()                  
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()   


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url, timeout=0)
    cart_page.no_products_in_cart()
    cart_page.cart_is_empty()


@pytest.mark.cart
class TestUserAddToCartFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/accounts/login/')
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = 'Q!W@E#R$t5y6u7i8'
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_not_be_success_message()   


    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.check_product_added_to_cart_message()
        page.check_product_name_added_to_cart()
        page.check_price_added_to_cart()

