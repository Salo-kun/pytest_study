from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), 'Busket message not equal empty'

    def no_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_CART), 'Busket not empty'