
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    NAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_FROM_HOME_BUTTON
)

from helpers import generate_email, generate_password


# Успешная регистрация
def test_registration_success(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    wait = WebDriverWait(driver, 10)

    # Открываем страницу входа
    wait.until(
        EC.element_to_be_clickable(LOGIN_FROM_HOME_BUTTON)
    ).click()

    # Переходим к регистрации
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
        )
    ).click()

    # Заполняем форму регистрации
    wait.until(
        EC.visibility_of_element_located(NAME_INPUT)
    ).send_keys("Yaroslav")

    driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*PASSWORD_INPUT).send_keys(generate_password())

    # Нажимаем кнопку регистрации
    driver.find_element(*REGISTER_BUTTON).click()

    # Проверяем переход на страницу входа
    wait.until(EC.url_contains("/login"))


# Проверка регистрации с коротким паролем
def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    wait = WebDriverWait(driver, 10)

    # Заполняем форму регистрации
    wait.until(
        EC.visibility_of_element_located(NAME_INPUT)
    ).send_keys("Yaroslav")

    driver.find_element(*EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*PASSWORD_INPUT).send_keys("12345")

    # Нажимаем кнопку регистрации
    driver.find_element(*REGISTER_BUTTON).click()

    # Проверяем сообщение об ошибке
    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
        )
    )

    assert error_message.is_displayed()
