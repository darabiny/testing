from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Page_Object import SearchHelper, SearchHelper_User_Table

# тесты страницы таблицы пользователей

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# тестируем состав меню на целостность
def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_users_table()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

# проверка на наличие всех предполагаемых элементов на странице
def test_user_table_elements(browser):
    main_page = SearchHelper_User_Table(browser)
    main_page.go_to_site_users_table()
    elements = main_page.elements()
    for i in elements:
        assert i.is_displayed()

# проверка на наличие в таблице добавленных данных
@pytest.mark.parametrize(
    "word",
    [
        '1@1 1 Женский 1.2 2.2, 2.3',
        '1@1 1 Женский 1.2 2.1, 2.2',
        '1@1 1 Женский 1.2 2.2',
        '1@1 1 Женский 1.2 2.1, 2.2, 2.3',
        '1@1 1 Мужской 1.1 2.1',
        '1@1 1 Мужской 1.1 2.1'
    ]
)
def test_user_table(browser, word):
    main_page = SearchHelper_User_Table(browser)
    main_page.go_to_site_users_table()
    assert main_page.dates(word) == 'yes'
