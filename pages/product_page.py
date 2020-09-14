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
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADD_TO_CART_MESSAGE).text, 'Product name in add message is wrong'

    def check_price_added_to_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.TOTAL_BUSKET).text, 'Poduct price in add message is wrong'