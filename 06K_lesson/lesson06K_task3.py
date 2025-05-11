from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buy_items():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    backpack_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    tshirt_button = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")

    backpack_button.click()
    tshirt_button.click()
    onesie_button.click()

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Петров")
    postal_code_input.send_keys("123456")
    continue_button.click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_info_label.summary_total_label")
        )
    )
    total_price_text = total_element.text

    expected_total = "Total: $58.29"
    assert total_price_text == expected_total, (
        f"Итоговая сумма '{total_price_text}' не соответствует "
        f"ожидаемой '{expected_total}'"
    )

    driver.quit()
