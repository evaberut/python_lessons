from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        self.result_field = self.driver.find_element(By.CSS_SELECTOR, "#result")
        self.button_7 = self.driver.find_element(By.ID, "btn7")
        self.button_plus = self.driver.find_element(By.ID, "btn+")
        self.button_8 = self.driver.find_element(By.ID, "btn8")
        self.button_equal = self.driver.find_element(By.ID, "btn=")

    def set_delay(self, delay: str):
        self.delay_input.send_keys(delay)

    def press_button(self, button: WebElement):
        button.click()

    def get_result(self) -> str:
        return self.result_field.text

    def perform_calculation(self, delay: str):
        self.set_delay(delay)
        self.press_button(self.button_7)
        self.press_button(self.button_plus)
        self.press_button(self.button_8)
        self.press_button(self.button_equal)

    def wait_for_result(self, expected_result: str, timeout: int):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#result"), expected_result)
        )
