from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click() 

    def should_be_same_name(self): 
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_IN_BASKET).text
        assert item_name == item_in_basket, "Wrong item in basket"

    def should_be_same_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert item_price == price_in_basket, "Wrong price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        
    def should_be_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"