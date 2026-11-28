from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    NAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_FROM_HOME_BUTTON,
    REGISTER_LINK,
    PASSWORD_ERROR_MESSAGE,
    LOGIN_PAGE_MARKER
)

from helpers import generate_email, generate_password
from urls import BASE_URL, REGISTER_URL


class TestRegistration:

    # Проверка успешной регистрации
    def test_registration_success(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable(LOGIN_FROM_HOME_BUTTON)
        ).click()

        wait.until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        wait.until(
            EC.visibility_of_element_located(NAME_INPUT)
        ).send_keys("Yaroslav")

        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_password())

        driver.find_element(*REGISTER_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(LOGIN_PAGE_MARKER)
        ).is_displayed()

    # Проверка регистрации с коротким паролем
    def test_registration_with_short_password(self, driver):
        driver.get(REGISTER_URL)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located(NAME_INPUT)
        ).send_keys("Yaroslav")

        driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")

        driver.find_element(*REGISTER_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(PASSWORD_ERROR_MESSAGE)
        ).is_displayed()