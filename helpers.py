
import random

from selenium.webdriver.support import expected_conditions as EC

from locators import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON
)
from urls import BASE_URL


# Генератор уникального email
def generate_email():
    number = random.randint(100, 999)
    return f"yaroslav_naumenko_59_{number}@yandex.ru"


# Генератор пароля
def generate_password():
    return "Test123456"


# Данные тестового аккаунта
EMAIL = "yaroslav_test_529@yandex.ru"
PASSWORD = "Test123456"


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
