from selenium.webdriver.common.by import By

class Locator_Authorization:
    LOCATOR_LOGIN = (By.ID, 'loginEmail')
    LOCATOR_PASSWORD = (By.ID, 'loginPassword')
    LOCATOR_ENTER = (By.CSS_SELECTOR, '.uk-button')
    LOCATOR_ERROR_LOGIN = (By.XPATH, '//*[@id="emailFormatError"]/p')
    LOCATOR_ERROR_PASSWORD = (By.XPATH, '//*[@id="KEKEKEKEKEKKEKE"]/p')
    LOCATOR_ERROR_LOGIN_CROSS = (By.CSS_SELECTOR, '.uk-alert-close')

class Locator_Menu:
    LOCATOR_AUTHORIZATION = (By.ID, "menuAuth")
    LOCATOR_MAIN = (By.ID, "menuMain")
    LOCATOR_USERS = (By.ID, "menuUsersOpener")
    LOCATOR_USERS_USER = (By.ID, "menuUsers")
    LOCATOR_USERS_USER_ADD = (By.ID, "menuUserAdd")
    LOCATOR_MORE = (By.ID, "menuMore")

class Locator_Main:
    LOCATOR_WELCOME = (By.TAG_NAME, "h3")
    LOCATOR_TEXT = (By.TAG_NAME, "p")
    LOCATOR_WISH = (By.XPATH, "/html/body/div[2]/div[2]/div/p[2]")
    LOCATOR_PICTURE = (By.CSS_SELECTOR, '.uk-cover')

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
    LOCATOR_WINDOW = (By.CSS_SELECTOR, '.uk-modal-body')
    LOCATOR_WINDOW_OK = (By.CSS_SELECTOR, '.uk-button.uk-button-primary.uk-modal-close')

class Locator_User_Table:
    LOCATOR_TABLE = (By.ID, 'dataTable')
    LOCATOR_BUTTON = (By.ID, 'addUser')
    LOCATOR_TABLE_DATE = (By.XPATH, '//*[@id="dataTable"]/tbody')


