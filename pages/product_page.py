from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def check_appeared_messages(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES_BLOCK), 'There are no messages appeared'

    def check_product_name_in_success_message(self, product_name):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name_in_message == product_name, f'Wrong product name "{product_name_in_message}" ' \
                                                        f'is shown is message. Expcted name was "{product_name}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"



