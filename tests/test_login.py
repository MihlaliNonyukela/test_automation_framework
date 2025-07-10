from selenium.webdriver.common.by import By
import pytest

def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    # Fill in username and password
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    # Verify success message
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
