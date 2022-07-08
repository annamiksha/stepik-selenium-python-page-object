from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_GO_TO_CART = (By.CSS_SELECTOR, '.basket-mini .btn-default:first-child')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    PASSWORD_REPEAT = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.NAME, 'registration_submit')
    MESSAGE_ERROR = (By.CLASS_NAME, 'alert-danger')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    MESSAGES_BLOCK = (By.ID, 'messages')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert-success:first-of-type strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
    BASKET_MESSAGE = (By.ID, 'messages')
