from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )

    wait = WebDriverWait(driver, 10)
    first_name_input = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    last_name_input = driver.find_element(By.NAME, "last-name")
    address_input = driver.find_element(By.NAME, "address")
    email_input = driver.find_element(By.NAME, "e-mail")
    phone_input = driver.find_element(By.NAME, "phone")
    zip_code_input = driver.find_element(By.NAME, "zip-code")
    city_input = driver.find_element(By.NAME, "city")
    country_input = driver.find_element(By.NAME, "country")
    job_position_input = driver.find_element(By.NAME, "job-position")
    company_input = driver.find_element(By.NAME, "company")
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Петров")
    address_input.send_keys("Ленина, 55-3")
    email_input.send_keys("test@skypro.com")
    phone_input.send_keys("+7985899998787")
    city_input.send_keys("Москва")
    country_input.send_keys("Россия")
    job_position_input.send_keys("QA")
    company_input.send_keys("SkyPro")

    submit_button.click()

    assert "is-invalid" in zip_code_input.get_attribute("class"), (
        "Поле Zip code не подсвечено красным"
    )
    assert "is-valid" in first_name_input.get_attribute("class"), (
        "Поле First name не подсвечено зеленым"
    )
    assert "is-valid" in last_name_input.get_attribute("class"), (
        "Поле Last name не подсвечено зеленым"
    )
    assert "is-valid" in address_input.get_attribute("class"), (
        "Поле Address не подсвечено зеленым"
    )
    assert "is-valid" in email_input.get_attribute("class"), (
        "Поле Email не подсвечено зеленым"
    )
    assert "is-valid" in phone_input.get_attribute("class"), (
        "Поле Phone number не подсвечено зеленым"
    )
    assert "is-valid" in city_input.get_attribute("class"), (
        "Поле City не подсвечено зеленым"
    )
    assert "is-valid" in country_input.get_attribute("class"), (
        "Поле Country не подсвечено зеленым"
    )
    assert "is-valid" in job_position_input.get_attribute("class"), (
        "Поле Job position не подсвечено зеленым"
    )
    assert "is-valid" in company_input.get_attribute("class"), (
        "Поле Company не подсвечено зеленым"
    )

    driver.quit()
