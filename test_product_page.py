from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

   
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Product Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()                # добавляем товар    
    page.solve_quiz_and_get_code()      # ждем код
    page.should_be_same_name()
    page.should_be_same_price()

