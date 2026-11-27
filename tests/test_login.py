
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    LOGIN_FROM_HOME_BUTTON,
    PERSONAL_ACCOUNT_LINK,
    LOGIN_LINK
)


EMAIL = "yaroslav_test_529@yandex.ru"
PASSWORD = "Test123456"

BASE_URL = "https://stellarburgers.education-services.ru/"


# Общая функция входа
def login(driver, wait):
    wait.until(
        EC.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys(EMAIL)

    wait.until(
        EC.visibility_of_element_located(PASSWORD_INPUT)
    ).send_keys(PASSWORD)

    wait.until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    ).click()

    wait.until(EC.url_to_be(BASE_URL))


# Ожидание полной загрузки страницы
def wait_for_page_load(driver, wait):
    wait.until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )


# Вход через кнопку «Войти в аккаунт» на главной
def test_login_from_home(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 30)
    wait_for_page_load(driver, wait)

    wait.until(
        EC.element_to_be_clickable(LOGIN_FROM_HOME_BUTTON)
    ).click()

    login(driver, wait)


# Вход через ссылку «Личный кабинет»
def test_login_from_personal_account(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 30)
    wait_for_page_load(driver, wait)

    wait.until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()

    login(driver, wait)


# Вход со страницы регистрации
def test_login_from_registration(driver):
    driver.get(BASE_URL + "register")

    wait = WebDriverWait(driver, 30)
    wait_for_page_load(driver, wait)

    wait.until(
        EC.element_to_be_clickable(LOGIN_LINK)
    ).click()

    login(driver, wait)


# Вход со страницы восстановления пароля
def test_login_from_password_recovery(driver):
    driver.get(BASE_URL + "forgot-password")

    wait = WebDriverWait(driver, 30)
    wait_for_page_load(driver, wait)

    # Ждём появления поля Email на странице восстановления пароля
    wait.until(
        EC.visibility_of_element_located(EMAIL_INPUT)
    )

    # Переходим на страницу входа
    wait.until(
        EC.element_to_be_clickable(LOGIN_LINK)
    ).click()

    login(driver, wait)
