import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

   
#def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                         # открываем страницу
#    page.add_to_basket()                # добавляем товар    
#    page.solve_quiz_and_get_code()      # ждем код
#    page.should_be_same_name()
#    page.should_be_same_price()


#@pytest.mark.parametrize('num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_guest_can_add_product_to_basket(browser, num):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
#    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                         # открываем страницу
#    page.add_to_basket()                # добавляем товар    
#    page.solve_quiz_and_get_code()      # ждем код
#    page.should_be_same_name()
#    page.should_be_same_price()
    
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                         # открываем страницу
#    page.add_to_basket()                # добавляем товар 
#    page.should_not_be_success_message()
    
    
#def test_guest_cant_see_success_message(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                         # открываем страницу
#    page.should_not_be_success_message()
    
    
#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                         # открываем страницу
#    page.add_to_basket()                # добавляем товар 
#    page.should_be_message_disappeared()
    
    
#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_login_link()
    
#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_login_page()
    
#def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_basket()
    # далее работаем с корзиной
#    basket_page = BasketPage(browser, browser.current_url)    
#    basket_page.should_not_be_items()
#    basket_page.should_be_msg_about_empty()
    
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"  
               
        # работаем со страницей логина
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, login_link) 
        login_page.open()        
        login_page.register_new_user()
        time.sleep(5)
        # проверка, что юзер залогинен
        login_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, self.link)    
        page.open()                         
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)   
        page.open()                         
        page.add_to_basket()              
        page.should_be_same_name()
        page.should_be_same_price()
    