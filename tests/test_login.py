from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    EMAIL_INPUT,
    LOGIN_FROM_HOME_BUTTON,
    PERSONAL_ACCOUNT_LINK,
    LOGIN_LINK
)

from helpers import login, wait_for_page_load
from urls import (
    BASE_URL,
    LOGIN_URL,
    REGISTER_URL,
    FORGOT_PASSWORD_URL
)


class TestLogin:

    # Вход через кнопку «Войти в аккаунт» на главной
    def test_login_from_home(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 30)
        wait_for_page_load(driver, wait)

        wait.until(
            EC.element_to_be_clickable(LOGIN_FROM_HOME_BUTTON)
        ).click()

        login(driver, wait)

        assert driver.current_url == BASE_URL

    # Вход через ссылку «Личный кабинет»
    def test_login_from_personal_account(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 30)
        wait_for_page_load(driver, wait)

        wait.until(
            EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
        ).click()

        login(driver, wait)

        assert driver.current_url == BASE_URL

    # Вход со страницы регистрации
    def test_login_from_registration(self, driver):
        driver.get(REGISTER_URL)

        wait = WebDriverWait(driver, 30)
        wait_for_page_load(driver, wait)

        wait.until(
            EC.element_to_be_clickable(LOGIN_LINK)
        ).click()

        assert driver.current_url == LOGIN_URL

        login(driver, wait)

        assert driver.current_url == BASE_URL

    # Вход со страницы восстановления пароля
    def test_login_from_password_recovery(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        wait = WebDriverWait(driver, 30)
        wait_for_page_load(driver, wait)

        wait.until(
            EC.visibility_of_element_located(EMAIL_INPUT)
        )

        wait.until(
            EC.element_to_be_clickable(LOGIN_LINK)
        ).click()

        assert driver.current_url == LOGIN_URL

        login(driver, wait)

        assert driver.current_url == BASE_URL