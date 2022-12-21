from .base_page import BasePage
from .locators import BasketPageLocators  
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
            "Items are presented, but should not be"
     
     
    def should_be_msg_about_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Empty message is not presented, but should be"