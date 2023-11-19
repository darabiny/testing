from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Page_Object import SearchHelper, SearchHelper_User_Add

# тесты страницы добавления пользователей

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# тестируем состав меню на целостность
def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_add_user()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

# проверка на наличие всех предполагаемых элементов на странице
def test_user_add_elements(browser):
    main_page = SearchHelper_User_Add(browser)
    main_page.go_to_site_add_user()
    elements = main_page.elements()
    for i in elements:
        assert i.is_displayed()

# тесты ввода
@pytest.mark.parametrize(
    "email, password, name, gender, var1, var2",
    [
        ('1@1', '', '', 'male', 1, 0),
        ('1@1', '1', '1', 'female', 2, 7),
        ('1@1', '', '', 'male', 1, 1),
        ('1@1', '1', '1', 'female', 2, 2),
        ('1@1', '', '', 'male', 1, 3),
        ('1@1', '1', '1', 'female', 2, 4),
        ('1@1', '', '', 'male', 1, 5),
        ('1@1', '1', '1', 'female', 2, 6),
        ('1', '1', '', 'female', 1, 4),
        ('1', '', '1', 'male', 2, 5),
        ('1', '1', '', 'female', 1, 6),
        ('1', '', '1', 'male', 2, 0),
        ('1', '1', '', 'female', 1, 7),
        ('1', '', '1', 'male', 2, 1),
        ('1', '1', '', 'female', 1, 2),
        ('1', '', '1', 'male', 2, 3),
        ('1@1', '1'*256, '1', 'male', 1, 1),
        ('1@1', '1', '1'*33, 'male', 1, 1)
    ]
)
def test_user_add(browser, email, password, name, gender, var1, var2):
    main_page = SearchHelper_User_Add(browser)
    main_page.go_to_site_add_user()
    ans = main_page.enter_data(email, password, name, gender, var1, var2)
    if email == '1':
        assert ans == 'Неверный формат E-Mail'
    elif name == '':
        assert ans == 'Поле Имя не может быть пустым'
    elif password == '':
        assert ans == 'Поле Пароль не может быть пустым'
    elif len(password) > 255:
        assert ans == 'ОШИБКА! undefined'
    elif len(name) > 30:
        assert ans == 'ОШИБКА! FAIL'
    else:
        assert ans == 'Данные добавлены.'

