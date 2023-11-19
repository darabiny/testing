from Base_Page import BasePage
from LOCATOR import Locator_Authorization, Locator_Main, Locator_Menu, Locator_User_Table, Locator_User_Add
from time import sleep

# здесь всё взаимодействие со страницей
# разделены по классам в зависимости от странички, действия которой, осуществляют

# для меню
class SearchHelper(BasePage):
    # def enter(self, word, locate):
    #     search_field = self.find_element(locate)
    #     search_field.send_keys(word)
    # def click_bate(self, locate):
    #     self.find_element(locate,time=2).click()
    # def show(self, locate):
    #     return self.find_element(locate)
    def menu_elements(self):
        search_field1 = self.find_element(Locator_Menu.LOCATOR_MAIN)
        search_field2 = self.find_element(Locator_Menu.LOCATOR_AUTHORIZATION)
        search_field3 = self.find_element(Locator_Menu.LOCATOR_MORE)
        search_field4 = self.find_element(Locator_Menu.LOCATOR_USERS)
        search_field4.click()
        sleep(1) # программа не успевает открыть окно
        search_field5 = self.find_element(Locator_Menu.LOCATOR_USERS_USER)
        search_field6 = self.find_element(Locator_Menu.LOCATOR_USERS_USER_ADD)
        return [search_field1, search_field2, search_field3, search_field4, search_field5, search_field6]

# для авторизации
class SearchHelper_Authoriztion(BasePage):
    def elements(self):
        login = self.find_element(Locator_Authorization.LOCATOR_LOGIN)
        password = self.find_element(Locator_Authorization.LOCATOR_PASSWORD)
        enter = self.find_element(Locator_Authorization.LOCATOR_ENTER)
        return [login, password, enter]
    def come_in_authorization(self, word_login, word_password):
        search_field = self.find_element(Locator_Authorization.LOCATOR_LOGIN)
        search_field.send_keys(word_login)
        search_field_pass = self.find_element(Locator_Authorization.LOCATOR_PASSWORD)
        search_field_pass.send_keys(word_password)
        self.find_element(Locator_Authorization.LOCATOR_ENTER, time=2).click()
    def show_main_welcome(self):
        return self.find_element(Locator_Main.LOCATOR_WELCOME)
    def show_authorization_login_error(self):
        return self.find_element(Locator_Authorization.LOCATOR_ERROR_LOGIN)
    def show_authorization_password_error(self):
        return self.find_element(Locator_Authorization.LOCATOR_ERROR_PASSWORD)
    def show_authorization_login_error_cross(self):
        self.find_element(Locator_Authorization.LOCATOR_ERROR_LOGIN_CROSS,time=2).click()
        sleep(1)
        return self.find_element(Locator_Authorization.LOCATOR_ERROR_LOGIN_CROSS)

# для главной страницы
class SearchHelper_Main(BasePage):
    def main(self):
        welcome = self.find_element(Locator_Main.LOCATOR_WELCOME)
        text = self.find_element(Locator_Main.LOCATOR_TEXT)
        wish = self.find_element(Locator_Main.LOCATOR_WISH)
        picture = self.find_element(Locator_Main.LOCATOR_PICTURE)
        return welcome, text, wish, picture

# для страницы добавления пользователя
class SearchHelper_User_Add(BasePage):
    def elements(self):
        email = self.find_element(Locator_User_Add.LOCATOR_EMAIL)
        password = self.find_element(Locator_User_Add.LOCATOR_PASSWORD)
        name = self.find_element(Locator_User_Add.LOCATOR_NAME)
        gender = self.find_element(Locator_User_Add.LOCATOR_GENDER)
        var11 = self.find_element(Locator_User_Add.LOCATOR_V1_1)
        var12 = self.find_element(Locator_User_Add.LOCATOR_V1_2)
        var21 = self.find_element(Locator_User_Add.LOCATOR_V2_1)
        var22 = self.find_element(Locator_User_Add.LOCATOR_V2_2)
        var23 = self.find_element(Locator_User_Add.LOCATOR_V2_3)
        enter = self.find_element(Locator_User_Add.LOCATOR_ENTER)
        return [email, password, name, gender, var11, var12, var21, var22, var23, enter]

    def enter_data(self, email, password, name, gen, var1, var2):
        search_field = self.find_element(Locator_User_Add.LOCATOR_EMAIL)
        search_field.send_keys(email)
        if password != '':
            search_field = self.find_element(Locator_User_Add.LOCATOR_PASSWORD)
            search_field.send_keys(password)
        if name != '':
            search_field = self.find_element(Locator_User_Add.LOCATOR_NAME)
            search_field.send_keys(name)
        if gen == 'female': self.find_element(Locator_User_Add.LOCATOR_GENDER_2).click()
        if var1 == 2: self.find_element(Locator_User_Add.LOCATOR_V1_2).click()
        if var2 == 0:
            self.find_element(Locator_User_Add.LOCATOR_V2_1).click()
        elif var2 == 7:
            self.find_element(Locator_User_Add.LOCATOR_V2_2).click()
            self.find_element(Locator_User_Add.LOCATOR_V2_3).click()
        elif var2 == 2:
            self.find_element(Locator_User_Add.LOCATOR_V2_1).click()
            self.find_element(Locator_User_Add.LOCATOR_V2_2).click()
        elif var2 == 3:
            self.find_element(Locator_User_Add.LOCATOR_V2_1).click()
            self.find_element(Locator_User_Add.LOCATOR_V2_3).click()
        elif var2 == 4:
            self.find_element(Locator_User_Add.LOCATOR_V2_2).click()
        elif var2 == 5:
            self.find_element(Locator_User_Add.LOCATOR_V2_3).click()
        elif var2 == 6:
            self.find_element(Locator_User_Add.LOCATOR_V2_1).click()
            self.find_element(Locator_User_Add.LOCATOR_V2_2).click()
            self.find_element(Locator_User_Add.LOCATOR_V2_3).click()
        self.find_element(Locator_User_Add.LOCATOR_ENTER, time=2).click()
        if email == '1':
            return self.find_element(Locator_User_Add.LOCATOR_ERROR_LOGIN).text
        elif name == '':
            return self.find_element(Locator_User_Add.LOCATOR_ERROR_NAME).text
        elif password == '':
            return self.find_element(Locator_User_Add.LOCATOR_ERROR_PASSWORD).text
        else:
            return self.find_element(Locator_User_Add.LOCATOR_WINDOW).text

# для страницы с таблицуй пользователей
class SearchHelper_User_Table(BasePage):
    def elements(self):
        button = self.find_element(Locator_User_Table.LOCATOR_BUTTON)
        table = self.find_element(Locator_User_Table.LOCATOR_TABLE)
        return [button, table]
    def dates(self, word):
        l = [str(i.text) for i in self.find_elements(Locator_User_Table.LOCATOR_TABLE_DATE)]
        l = l[0].split('\n')
        if word in l:
            return 'yes'
        else:
            return 'no'





