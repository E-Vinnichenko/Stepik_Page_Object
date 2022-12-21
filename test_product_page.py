import pytest
from .pages.product_page import ProductPage
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
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()                # добавляем товар 
    page.should_not_be_success_message()
    
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_not_be_success_message()
    
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()                # добавляем товар 
    page.should_be_message_disappeared()