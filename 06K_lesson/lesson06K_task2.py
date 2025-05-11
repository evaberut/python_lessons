from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")

    button_7.click()
    button_plus.click()
    button_8.click()
    button_equals.click()

    result_display = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    assert result_display, "Результат на экране не соответствует ожидаемому"

    driver.quit()
