from Page_Object import SearchHelper, SearchHelper_User_Table
from time import sleep


def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_users_menu()
    sleep(5)
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

def test_user_table_elements(browser):
    main_page = SearchHelper_User_Table(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_users()
    elements = main_page.elements()
    for i in elements:
        assert i.is_displayed()

