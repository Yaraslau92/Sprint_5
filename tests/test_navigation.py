
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    PERSONAL_ACCOUNT_LINK,
    CONSTRUCTOR_LINK,
    LOGO_LINK
)


# Данные тестового аккаунта
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


# Проверка перехода в личный кабинет
def test_open_personal_account(driver):
    driver.get(BASE_URL + "login")

    wait = WebDriverWait(driver, 20)

    login(driver, wait)

    wait.until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()

    wait.until(EC.url_contains("/account"))


# Проверка перехода в конструктор через кнопку «Конструктор»
def test_constructor_button_from_account(driver):
    driver.get(BASE_URL + "login")

    wait = WebDriverWait(driver, 20)

    login(driver, wait)

    wait.until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()

    wait.until(EC.url_contains("/account"))

    wait.until(
        EC.element_to_be_clickable(CONSTRUCTOR_LINK)
    ).click()

    wait.until(EC.url_to_be(BASE_URL))


# Проверка перехода в конструктор через логотип
def test_logo_from_account(driver):
    driver.get(BASE_URL + "login")

    wait = WebDriverWait(driver, 20)

    login(driver, wait)

    wait.until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()

    wait.until(EC.url_contains("/account"))

    wait.until(
        EC.element_to_be_clickable(LOGO_LINK)
    ).click()

    wait.until(EC.url_to_be(BASE_URL))


# Проверка выхода из аккаунта
def test_logout(driver):
    driver.get(BASE_URL + "login")

    wait = WebDriverWait(driver, 20)

    login(driver, wait)

    wait.until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()

    wait.until(EC.url_contains("/account"))

    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Выход']")
        )
    )

    logout_button.click()

    wait.until(EC.url_contains("/login"))
