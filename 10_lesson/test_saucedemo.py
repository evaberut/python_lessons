import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("Покупка товаров")
class TestSauceDemo:
    @allure.title("Покупка товаров")
    @allure.description("Проверка процесса покупки товаров на сайте")
    @allure.severity(Severity.CRITICAL)
    def test_buy_items(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open()

        with allure.step("Ввод логина и пароля"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")

        with allure.step("Нажатие на кнопку логина"):
            login_page.click_login()

        with allure.step("Добавление товаров в корзину"):
            inventory_page.add_backpack_to_cart()
            inventory_page.add_tshirt_to_cart()
            inventory_page.add_onesie_to_cart()

        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Проверка наличия товаров в корзине"):
            assert cart_page.is_backpack_in_cart(), (
                "Рюкзак должен быть в корзине"
            )
            assert cart_page.is_tshirt_in_cart(), (
                "Футболка должна быть в корзине"
            )
            assert cart_page.is_onesie_in_cart(), (
                "Комбинезон должен быть в корзине"
            )

        with allure.step("Нажатие на кнопку Checkout"):
            cart_page.click_checkout()

        with allure.step("Ввод информации о доставке"):
            checkout_page.enter_first_name("Иван")
            checkout_page.enter_last_name("Иванов")
            checkout_page.enter_postal_code("123456")

        with allure.step("Нажатие на кнопку Continue"):
            checkout_page.click_continue()

        with allure.step("Получение и проверка итоговой суммы"):
            total_text = checkout_page.get_total()
            total_value = float(total_text.split("$")[1])
            assert (
                total_value == 58.29
            ), f"Ожидаемая сумма: $58.29, фактическая: ${total_value}"
