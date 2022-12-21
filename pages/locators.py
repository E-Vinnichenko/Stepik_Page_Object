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


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a") 
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    
class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p") 
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    REGISTRATION_INPUT1 = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_INPUT2 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_INPUT3 = (By.CSS_SELECTOR, "#id_registration-password2")  
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button")