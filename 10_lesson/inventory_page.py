from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        backpack_button = self.driver.find_element(*self.add_backpack_button)
        backpack_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"),
                "1",
            )
        )

    def add_tshirt_to_cart(self):
        tshirt_button = self.driver.find_element(*self.add_tshirt_button)
        tshirt_button.click()

    def add_onesie_to_cart(self):
        onesie_button = self.driver.find_element(*self.add_onesie_button)
        onesie_button.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(*self.cart_link)
        cart_link.click()
