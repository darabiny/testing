from selenium.webdriver.common.by import By

# здесь все локаторы которые я использую в скриптах
# они разделены по классам, в зависимости от того к какой страничке принадлежат
# постарался сделать говорящие значения, чтобы было понятней: что, куда и откуда идёт

# страница авторизации
class Locator_Authorization:
    LOCATOR_LOGIN = (By.ID, 'loginEmail')
    LOCATOR_PASSWORD = (By.ID, 'loginPassword')
    LOCATOR_ENTER = (By.CSS_SELECTOR, '.uk-button')
    LOCATOR_ERROR_LOGIN = (By.XPATH, '//*[@id="emailFormatError"]/p')
    LOCATOR_ERROR_PASSWORD = (By.XPATH, '//*[@id="KEKEKEKEKEKKEKE"]/p')
    LOCATOR_ERROR_LOGIN_CROSS = (By.CSS_SELECTOR, '.uk-alert-close')

# локаторы меню которое находится в верху каждой странички, кроме авторизации
class Locator_Menu:
    LOCATOR_AUTHORIZATION = (By.ID, "menuAuth")
    LOCATOR_MAIN = (By.ID, "menuMain")
    LOCATOR_USERS = (By.ID, "menuUsersOpener")
    LOCATOR_USERS_USER = (By.ID, "menuUsers")
    LOCATOR_USERS_USER_ADD = (By.ID, "menuUserAdd")
    LOCATOR_MORE = (By.ID, "menuMore")

# страница главная
class Locator_Main:
    LOCATOR_WELCOME = (By.TAG_NAME, "h3")
    LOCATOR_TEXT = (By.XPATH, "/html/body/div[2]/div[2]/div/p[1]")
    LOCATOR_WISH = (By.XPATH, "/html/body/div[2]/div[2]/div/p[2]")
    LOCATOR_PICTURE = (By.CSS_SELECTOR, '.uk-cover')

# страница добавления пользователя
class Locator_User_Add:
    LOCATOR_EMAIL = (By.ID, "dataEmail")
    LOCATOR_PASSWORD = (By.ID, "dataPassword")
    LOCATOR_NAME = (By.ID, "dataName")
    LOCATOR_GENDER = (By.ID, "dataGender")
    LOCATOR_GENDER_1 = (By.XPATH, '//*[@id="dataGender"]/option[1]')
    LOCATOR_GENDER_2 = (By.XPATH, '//*[@id="dataGender"]/option[2]')
    LOCATOR_V1_1 = (By.ID, "dataSelect11")
    LOCATOR_V1_2 = (By.ID, "dataSelect12")
    LOCATOR_V2_1 = (By.ID, "dataSelect21")
    LOCATOR_V2_2 = (By.ID, "dataSelect22")
    LOCATOR_V2_3 = (By.ID, "dataSelect23")
    LOCATOR_ENTER = (By.ID, "dataSend")
    LOCATOR_ERROR_LOGIN = (By.XPATH, '//*[@id="emailFormatError"]/p')
    LOCATOR_ERROR_NAME = (By.XPATH, '//*[@id="blankNameError"]/p')
    LOCATOR_ERROR_PASSWORD = (By.XPATH, '//*[@id="blankPasswordError"]/p')
    LOCATOR_WINDOW = (By.XPATH, '/html/body/div[3]/div/div[1]')
    LOCATOR_WINDOW_CSS = (By.CSS_SELECTOR, 'uk-modal')
    LOCATOR_WINDOW_OK = (By.XPATH, '/html/body/div[3]/div/div[2]/button')

# страница таблицы пользователей
class Locator_User_Table:
    LOCATOR_TABLE = (By.ID, 'dataTable')
    LOCATOR_BUTTON = (By.ID, 'addUser')
    LOCATOR_TABLE_DATE = (By.XPATH, '//*[@id="dataTable"]/tbody')


