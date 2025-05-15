from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.ID, "n7")
        self.button_plus = (By.ID, "plus")
        self.button_8 = (By.ID, "n8")
        self.button_equals = (By.ID, "equal")
        self.result_output = (By.ID, "result")

    def open(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(url + "slow-calculator.html")

    def set_delay(self, delay: str):
        wait = WebDriverWait(self.driver, 10)
        delay_field = wait.until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(delay)

    def press_button(self, button_locator: tuple):
        wait = WebDriverWait(self.driver, 20)
        button = wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_result(self, timeout: int = 10) -> str:
        wait = WebDriverWait(self.driver, timeout)
        result_element = wait.until(
            EC.visibility_of_element_located(self.result_output)
        )
        return result_element.text

    def press_7(self):
        self.press_button(self.button_7)

    def press_plus(self):
        self.press_button(self.button_plus)

    def press_8(self):
        self.press_button(self.button_8)

    def press_equals(self):
        self.press_button(self.button_equals)
