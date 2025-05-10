from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    login_button.click()

    time.sleep(1)

    success_message = driver.find_element(By.ID, "flash")

    print(success_message.text)

finally:
    driver.quit()
