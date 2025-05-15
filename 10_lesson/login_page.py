from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        username_field = self.driver.find_element(*self.username_input)
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.driver.find_element(*self.password_input)
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
