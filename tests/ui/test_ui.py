import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    #Знаходимо поле, в якому будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    #Знаходимо кнопку Sing in
    btn_elem = driver.find_element(By.NAME, "commit")

    #Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub \xb7 GitHub"
    time.sleep(3)
    
    #Закріваємо браузер
    driver.close()

@pytest.mark.ui	
def test_check_search_TTN():
	#Створення об'єкту для керування браузером
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	
	#Відкриваємо сторінку https://tracking.novaposhta.ua/#/uk
	driver.get("https://tracking.novaposhta.ua/#/uk")
	
	#Знаходимо поле вводу ТТН
	search_elem = driver.find_element(By.ID, "en")
	
	#Вводимо неправильний номер ТТН
	search_elem.send_keys("12345678912345")
	
	#Знаходимо кнопку Пошук
	btn_elem = driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
	
	#Емулюємо клік лівою кнопкою мишки
	btn_elem.click()
	
	#Перевіряємо, що назва сторінки така, яку ми очікуємо
	assert driver.title == "Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН"
	time.sleep(3)
    
	#Закріваємо браузер
	driver.close()
      


      