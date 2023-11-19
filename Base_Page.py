from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# здесь вся работа с браузером

class BasePage:
    # драйвер и url каждой из страничек
    def __init__(self, driver):
        self.driver = driver
        self.base_url_authorization = "http://149.255.118.78:7080"
        self.base_url_main = "http://149.255.118.78:7080/main"
        self.base_url_more = "http://149.255.118.78:7080/more"
        self.base_url_users = "http://149.255.118.78:7080/users"
        self.base_url_add_user = "http://149.255.118.78:7080/add_user"

    def find_element(self, locator,time=5):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def go_to_site_authorization(self):
        return self.driver.get(self.base_url_authorization)
    def go_to_site_main(self):
        return self.driver.get(self.base_url_main)
    def go_to_site_more(self):
        return self.driver.get(self.base_url_more)
    def go_to_site_users_table(self):
        return self.driver.get(self.base_url_users)
    def go_to_site_add_user(self):
        return self.driver.get(self.base_url_add_user)