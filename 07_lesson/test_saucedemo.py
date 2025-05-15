import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_buy_items(self):
        self.login_page.open()

        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.add_tshirt_to_cart()
        self.inventory_page.add_onesie_to_cart()

        self.inventory_page.go_to_cart()
        self.assertTrue(
            self.cart_page.is_backpack_in_cart(),
            "Рюкзак должен быть в корзине",
        )
        self.assertTrue(
            self.cart_page.is_tshirt_in_cart(),
            "Футболка должна быть в корзине",
        )
        self.assertTrue(
            self.cart_page.is_onesie_in_cart(),
            "Комбинезон должен быть в корзине",
        )

        self.cart_page.click_checkout()

        self.checkout_page.enter_first_name("Иван")
        self.checkout_page.enter_last_name("Иванов")
        self.checkout_page.enter_postal_code("123456")
        self.checkout_page.click_continue()

        total_text = self.checkout_page.get_total()
        total_value = float(total_text.split('$')[1])

        self.assertEqual(
            total_value,
            58.29,
            f"Ожидаемая сумма: $58.29, фактическая: ${total_value}"
            )


if __name__ == "__main__":
    unittest.main()
