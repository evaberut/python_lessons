from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.backpack_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Backpack')]]",
        )
        self.tshirt_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Bolt T-Shirt')]]",
        )
        self.onesie_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Onesie')]]",
        )

    def click_checkout(self):
        checkout_button = self.driver.find_element(*self.checkout_button)
        checkout_button.click()

    def is_backpack_in_cart(self):
        try:
            self.driver.find_element(*self.backpack_in_cart)
            return True
        except NoSuchElementException:
            return False

    def is_tshirt_in_cart(self):
        try:
            self.driver.find_element(*self.tshirt_in_cart)
            return True
        except NoSuchElementException:
            return False

    def is_onesie_in_cart(self):
        try:
            self.driver.find_element(*self.onesie_in_cart)
            return True
        except NoSuchElementException:
            return False
