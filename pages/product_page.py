from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart_button.click()


    def check_product_added_to_cart_message(self):
        assert 'added to your basket' in self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE).text, 'No added to basket message'

    def check_product_name_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_add_to_cart_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADD_TO_CART_MESSAGE).text
        assert product_name == product_name_in_add_to_cart_message, \
            f'Product name in add message is wrong. Name: {product_name}, Name in cart message: {product_name_in_add_to_cart_message}'

    def check_price_added_to_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_busket = self.browser.find_element(*ProductPageLocators.TOTAL_BUSKET).text
        assert product_price == total_busket, f'Poduct price in add message is wrong. Price: {product_price}, Busket: {total_busket} '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_must_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_MESSAGE), \
            "Success message is not disappered"