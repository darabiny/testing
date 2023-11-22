from Page_Object import SearchHelper, SearchHelper_Main

def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_main_menu()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

def test_main_page(browser):
    main_page = SearchHelper_Main(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_main()
    welcome, text, wish, picture = main_page.main()
    assert welcome.is_displayed()
    assert welcome.text == 'Добро пожаловать!'
    assert text.is_displayed()
    assert text.text == 'Это - демо-сайт для проекта автотестов, написанный в качестве иллюстрации к статье на Хабре. Сайт прост и малофункционален, так как сделан не ради функционала, а ради тестов.'
    assert wish.is_displayed()
    assert wish.text == 'Да пребудет с нами TDD :)'
    assert picture.is_displayed()






