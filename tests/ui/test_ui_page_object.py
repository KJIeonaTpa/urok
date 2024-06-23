from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import SearchTTN
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #Створеня об'єкту сторінки
    sign_in_page = SignInPage()

    #відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    #викоуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title ("Sign in to GitHub \xb7 GitHub")

    #Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_check_incorrect_TTN_page_object():
    #Створеня об'єкту сторінки
    search_ttn = SearchTTN()

    #відкриваємо сторінку
    search_ttn.go_to()

    #виконуємо спробу пошуку ттн
    search_ttn.try_search("12345678912345")

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert search_ttn.check_title ("Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН")

    #Закриваємо браузер
    search_ttn.close()



