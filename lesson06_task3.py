from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
    )

    wait = WebDriverWait(driver, 20)
    images = driver.find_elements(By.TAG_NAME, 'img')
    for image in images:
        wait.untilwait.until(
            lambda driver: driver.execute_script(
                'return arguments[0].complete '
                '&& arguments[0].naturalWidth > 0',
                image
             )
        )

    third_image_src = images[2].get_attribute('src')

    print(third_image_src)

finally:
    driver.quit()
