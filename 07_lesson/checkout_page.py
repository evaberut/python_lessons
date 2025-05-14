from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (
            By.XPATH, "//div[@class='summary_info_label summary_total_label']"
            )

    def enter_first_name(self, first_name: str):
        first_name_field = self.driver.find_element(*self.first_name_input)
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code: str):
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.driver.find_element(*self.continue_button)
        continue_button.click()

    def get_total(self) -> str:
        total_element = self.driver.find_element(*self.total_label)
        return total_element.text
