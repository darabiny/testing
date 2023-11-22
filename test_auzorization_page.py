import pytest
from contextlib import nullcontext as does_not_raise
from Page_Object import SearchHelper_Authoriztion
from test_main_page import test_main_page

def test_elements(browser):
    main_page = SearchHelper_Authoriztion(browser)
    main_page.go_to_site_authorization()
    for i in main_page.elements():
        assert i.is_displayed()


@pytest.mark.parametrize(
    "login, password, expectation",
    [
        ("test@protei.ru", "test", does_not_raise()),
        ('g', 'g', pytest.raises(Exception)),
        ('h', None, pytest.raises(Exception)),
        (None, 'j', pytest.raises(TypeError)),
        (None, None, pytest.raises(TypeError))

    ]
)
def test_authorization_page(login, password, expectation, browser):
    with expectation:
        error = 0
        l = ['.com', '.ru', '.net', '.info', '.org', '.рф', '.дети']
        if login[0] == '@' or '.' not in login or '@' not in login or login[login.index('.'):] not in l or login[login.index('.') - 1] == '@':
            error = 1
        assert error == 0
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