from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from contextlib import nullcontext as does_not_raise
from Page_Object import SearchHelper_Authoriztion
from test_main_page import test_main_page

# тесты страницы автоматизации

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# проверка на наличие всех предполагаемых элементов на странице
def test_elements(browser):
    main_page = SearchHelper_Authoriztion(browser)
    main_page.go_to_site_authorization()
    for i in main_page.elements():
        assert i.is_displayed()


# тесты ввода
@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ("test@protei.ru", "test", does_not_raise()),
        ('g', 'g', pytest.raises(Exception)),
        ('h', None, pytest.raises(TypeError)),
        (None, 'j', pytest.raises(TypeError)),
        (None, None, pytest.raises(TypeError))

    ]
)
def test_authorization_page(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper_Authoriztion(browser)
        main_page.go_to_site_authorization()
        main_page.come_in_authorization(login, password)
        main_title = main_page.show_main_welcome()
        assert main_title.is_displayed()
        assert main_title.text == "Добро пожаловать!"
        test_main_page(browser) # проверка на целостность main page


@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h', 'h', does_not_raise()),
        ('@', 'h', does_not_raise()),
        ('h@', 'h', does_not_raise()),
        ('h@h', 'h', pytest.raises(Exception))
    ]
)
def test_authorization_page_login_error(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper_Authoriztion(browser)
        main_page.go_to_site_authorization()
        main_page.come_in_authorization(login, password)
        assert main_page.show_authorization_login_error().is_displayed()
        assert main_page.show_authorization_login_error().text == "Неверный формат E-Mail"

@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h@h', 'h', does_not_raise())
    ]
)
def test_authorization_page_password_error(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper_Authoriztion(browser)
        main_page.go_to_site_authorization()
        main_page.come_in_authorization(login, password)
        assert main_page.show_authorization_password_error().text == "Неверный E-Mail или пароль"

@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h', 'h', pytest.raises(Exception)),
    ]
)
def test_authorization_page_login_cross(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper_Authoriztion(browser)
        main_page.go_to_site_authorization()
        main_page.come_in_authorization(login, password)
        assert main_page.show_authorization_login_error_cross().is_displayed()