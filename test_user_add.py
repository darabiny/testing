import pytest
from Page_Object import SearchHelper, SearchHelper_User_Add

def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_user_add_menu()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

def test_user_add_elements(browser):
    main_page = SearchHelper_User_Add(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_user_add()
    elements = main_page.elements()
    for i in elements:
        assert i.is_displayed()

@pytest.mark.parametrize(
    "email, password, name, gender, var1, var2",
    [
        ('1@1', '', '', 'Мужской', '1.1', ''),
        ('1@1', '1', '1', 'Женский', '1.2', '2.1, 2.2, 2.3'),
        ('1@1', '', '', 'Мужской', '1.1', '2.1'),
        ('1@1', '1', '1', 'Женский', '1.2', '2.2'),
        ('1@1', '', '', 'Мужской', '1.1', '2.3'),
        ('1@1', '1', '1', 'Женский', '1.2', '2.1, 2.2'),
        ('1@1', '', '', 'Мужской', '1.1', '2.1, 2.3'),
        ('1@1', '1', '1', 'Женский', '1.2', '2.2, 2.3'),
        ('1', '1', '', 'Женский', '1.1', '2.1, 2.2'),
        ('1', '', '1', 'Мужской', '1.2', '2.1, 2.3'),
        ('1', '1', '', 'Женский', '1.1', '2.2, 2.3'),
        ('1', '', '1', 'Мужской', '1.2', ''),
        ('1', '1', '', 'Женский', '1.1', '2,1, 2.2, 2.3'),
        ('1', '', '1', 'Мужской', '1.2', '2.1'),
        ('1', '1', '', 'Женский', '1.1', '2.2'),
        ('1', '', '1', 'Мужской', '1.2', '2.3'),
        ('1@1', '1'*256, '1', 'Мужской', '1.1', ''),
        ('1@1', '1', '1'*33, 'Мужской', '1.1', '')
    ]
)
def test_user_add(browser, email, password, name, gender, var1, var2):
    main_page = SearchHelper_User_Add(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_user_add()
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
        assert main_page.go_table(f'{email} {name} {gender} {var1} {var2}') == 'yes'
        assert main_page.go_auz(email, password) == "Добро пожаловать!"


