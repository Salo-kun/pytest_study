import pytest
from pages.product_page import ProductPage
import time

def  test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_product_added_to_cart_message()
    page.check_product_name_added_to_cart()
    page.check_price_added_to_cart()
    
