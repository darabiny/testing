from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from contextlib import nullcontext as does_not_raise
from LOCATOR import Locator_Authorization
from Page_Object import SearchHelper
from time import sleep

# фикстура для работы с браузером
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

# фуекция котора выполняет ввод данных и запускает авторизацию
def come_in(login, password, main_page):
    main_page.go_to_site_authorization()
    main_page.enter(login, Locator_Authorization.LOCATOR_LOGIN)
    main_page.enter(password, Locator_Authorization.LOCATOR_PASSWORD)
    main_page.click_bate(Locator_Authorization.LOCATOR_ENTER)


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
        main_page = SearchHelper(browser)
        come_in(login, password, main_page)
        main_title = main_page.show(Locator_Authorization.LOCATOR_WELCOME)
        assert main_title.is_displayed()
        assert main_title.text == "Добро пожаловать!"


@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h', 'h', does_not_raise()),
        ('@', 'h', does_not_raise()),
        ('h@', 'h', does_not_raise()),
        ('h@h', 'h', pytest.raises(Exception))
    ]
)
def test_authorization_page_login(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper(browser)
        come_in(login, password, main_page)
        assert main_page.show(Locator_Authorization.LOCATOR_ERROR_LOGIN).is_displayed()
        assert main_page.show(Locator_Authorization.LOCATOR_ERROR_LOGIN).text == "Неверный формат E-Mail"

@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h', 'h', pytest.raises(Exception)),
    ]
)
def test_authorization_page_login_cross(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper(browser)
        come_in(login, password, main_page)
        main_page.click_bate(Locator_Authorization.LOCATOR_ERROR_LOGIN_CROSS)
        sleep(1) # здесь приходится использовать слип так как без него тест находит закрытый элемент
        assert main_page.show(Locator_Authorization.LOCATOR_ERROR_LOGIN).is_displayed()

@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ('h@h', 'h', does_not_raise())
    ]
)
def test_authorization_page_password(login, password, expectation, browser):
    with expectation:
        main_page = SearchHelper(browser)
        come_in(login, password, main_page)
        assert main_page.show(Locator_Authorization.LOCATOR_ERROR_PASSWORD).text == "Неверный E-Mail или пароль"