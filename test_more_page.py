from Page_Object import SearchHelper, SearchHelper_Main


def test_menu(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_more_menu()
    elements = main_page.menu_elements()
    for i in elements:
        assert i.is_displayed()

def test_more(browser):
    main_page = SearchHelper_Main(browser)
    main_page.go_to_site_authorization()
    main_page.go_to_more()
    welcome, text, wish, picture = main_page.main()
    assert welcome.is_displayed()
    assert welcome.text == 'НТЦ ПРОТЕЙ'
    assert text.is_displayed()
    assert text.text == 'Нет, лисичка не логотип Протея, логотип Протея вот такой.'
    assert wish.is_displayed()
    assert wish.text == 'Лисички нравятся лично автору. Всем фыр ^^'
    assert picture.is_displayed()