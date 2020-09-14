from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div")
    TOTAL_BUSKET = (By.CSS_SELECTOR, "#messages>div.alert>div>p:nth-child(1)>strong")
    