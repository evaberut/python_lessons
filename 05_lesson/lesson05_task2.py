from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = driver.find_element(
        By.XPATH,
        "//button[text()='Button with Dynamic ID']"
    )

    blue_button.click()

    time.sleep(1)

finally:
    driver.quit()
