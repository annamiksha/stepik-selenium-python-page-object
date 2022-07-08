from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    MESSAGES_BLOCK = (By.ID, 'messages')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert-success:first-of-type strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
