from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Page_Object import SearchHelper, SearchHelper_Main

# тесты страницы главной

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# тестируем состав меню на целостность
def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_main()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()



# тестируем главную страницу на целостность
def test_main_page(browser):
    main_page = SearchHelper_Main(browser)
    main_page.go_to_site_main()
    welcome, text, wish, picture = main_page.main()
    assert welcome.is_displayed()
    assert welcome.text == 'Добро пожаловать!'
    assert text.is_displayed()
    assert text.text == 'Это - демо-сайт для проекта автотестов, написанный в качестве иллюстрации к статье на Хабре. Сайт прост и малофункционален, так как сделан не ради функционала, а ради тестов.'
    assert wish.is_displayed()
    assert wish.text == 'Да пребудет с нами TDD :)'
    assert picture.is_displayed()






