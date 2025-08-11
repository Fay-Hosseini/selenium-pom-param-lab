from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.ID, "flash")

    def open(self,url):
        self.driver.get(url)

    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.error_message)
        )
        return self.driver.find_element(*self.error_message).text



