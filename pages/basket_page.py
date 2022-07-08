from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'Basket should be empty, but it is not'

    def check_if_empty_basket_text_is_visible(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            'Message expected to be visible, but it is not'
