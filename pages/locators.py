from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_page h1")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")
