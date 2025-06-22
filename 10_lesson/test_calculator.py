import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def browser():
    with allure.step("Инициализация браузера"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.implicitly_wait(10)
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.feature("Калькулятор")
class TestCalculator:

    @allure.title("Проверка сложения двух чисел")
    @allure.description(
        "Тест проверяет корректность сложения 7 и 8 с задержкой в 45 секунд."
    )
    @allure.severity(Severity.CRITICAL)
    def test_addition(self, browser):
        calculator_page = CalculatorPage(browser)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки в 45 секунд"):
            calculator_page.set_delay("45")

        with allure.step("Нажатие на '7'"):
            calculator_page.press_7()

        with allure.step("Нажатие на '+'"):
            calculator_page.press_plus()

        with allure.step("Нажатие на '8'"):
            calculator_page.press_8()

        with allure.step("Нажатие на '='"):
            calculator_page.press_equals()

        with allure.step("Получение результата и проверка"):
            result = calculator_page.get_result(timeout=60)
            assert result == "15", (
                f"Ожидаемый результат '15', но получен '{result}'"
            )
