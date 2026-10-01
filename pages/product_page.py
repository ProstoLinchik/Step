from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_added_product_name(self, product_name):
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert added_name == product_name, \
            f"Expected '{product_name}' in the added to basket message, got '{added_name}'"

    def should_be_basket_total_equal_to(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert basket_total == product_price, \
            f"Expected basket total {product_price}, got {basket_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still presented, but should have disappeared"