from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    PERSONAL_ACCOUNT_LINK,
    CONSTRUCTOR_LINK,
    LOGO_LINK,
    LOGOUT_BUTTON
)

from helpers import login
from urls import (
    BASE_URL,
    LOGIN_URL,
    ACCOUNT_URL
)


class TestNavigation:

    # Проверка перехода в личный кабинет
    def test_open_personal_account(self, driver):
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 20)
        login(driver, wait)

        wait.until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
        ).click()

        assert wait.until(EC.url_to_be(ACCOUNT_URL))

    # Проверка перехода в конструктор через кнопку «Конструктор»
    def test_constructor_button_from_account(self, driver):
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 20)
        login(driver, wait)

        wait.until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
        ).click()

        wait.until(
            EC.element_to_be_clickable(CONSTRUCTOR_LINK)
        ).click()

        assert wait.until(EC.url_to_be(BASE_URL))

    # Проверка перехода в конструктор через логотип
    def test_logo_from_account(self, driver):
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 20)
        login(driver, wait)

        wait.until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LOGO_LINK)
        ).click()

        assert wait.until(EC.url_to_be(BASE_URL))

    # Проверка выхода из аккаунта
    def test_logout(self, driver):
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 20)
        login(driver, wait)

        wait.until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()

        assert wait.until(EC.url_to_be(LOGIN_URL))