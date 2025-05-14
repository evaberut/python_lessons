import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )
        self.calculator_page = CalculatorPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        self.calculator_page.open()
        self.calculator_page.set_delay("45")
        self.calculator_page.press_7()
        self.calculator_page.press_plus()
        self.calculator_page.press_8()
        self.calculator_page.press_equals()
        time.sleep(45)
        result = self.calculator_page.get_result(timeout=50)
        self.assertEqual(result, "15")


if __name__ == "__main__":
    unittest.main()
