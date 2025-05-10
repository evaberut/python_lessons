from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")

    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    blue_button.click()

    time.sleep(10)

finally:
    driver.quit()
