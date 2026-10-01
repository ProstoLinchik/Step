from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_product_added(self):
        product_name = self.get_product_name()
        added_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == added_product_name, (
            f"Имя товара '{added_product_name}' не совпадает с ожидаемым '{product_name}'"
        )

    def should_be_basket_total_matches_product_price(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert product_price == basket_total, (
            f"Стоимость корзины '{basket_total}' не совпадает с ценой товара '{product_price}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"