from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Page_Object import SearchHelper, SearchHelper_Main


# тесты страницы для страницы вариантов

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# тестируем состав меню на целостность
def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_more()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

# проверка на наличие всех предполагаемых элементов на странице
def test_more(browser):
    main_page = SearchHelper_Main(browser)
    main_page.go_to_site_more()
    welcome, text, wish, picture = main_page.main()
    assert welcome.is_displayed()
    assert welcome.text == 'НТЦ ПРОТЕЙ'
    assert text.is_displayed()
    assert text.text == 'Нет, лисичка не логотип Протея, логотип Протея вот такой.'
    assert wish.is_displayed()
    assert wish.text == 'Лисички нравятся лично автору. Всем фыр ^^'
    assert picture.is_displayed()