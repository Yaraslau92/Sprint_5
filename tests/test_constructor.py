
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
    ACTIVE_TAB_CLASS
)


BASE_URL = "https://stellarburgers.education-services.ru/"


# Проверка переключения на вкладку «Булки»
def test_switch_to_buns(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 30)

    buns_tab = wait.until(
        EC.visibility_of_element_located(BUNS_TAB)
    )

    # Проверяем, активна ли вкладка «Булки»
    if ACTIVE_TAB_CLASS not in buns_tab.get_attribute("class"):
        wait.until(
            EC.element_to_be_clickable(BUNS_TAB)
        ).click()

    # Проверяем, что вкладка стала активной
    wait.until(
        lambda d: ACTIVE_TAB_CLASS in d.find_element(
            *BUNS_TAB
        ).get_attribute("class")
    )


# Проверка переключения на вкладку «Соусы»
def test_switch_to_sauces(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 30)

    sauces_tab = wait.until(
        EC.element_to_be_clickable(SAUCES_TAB)
    )

    # Нажимаем на вкладку
    sauces_tab.click()

    # Проверяем, что вкладка стала активной
    wait.until(
        lambda d: ACTIVE_TAB_CLASS in d.find_element(
            *SAUCES_TAB
        ).get_attribute("class")
    )


# Проверка переключения на вкладку «Начинки»
def test_switch_to_fillings(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 30)

    fillings_tab = wait.until(
        EC.element_to_be_clickable(FILLINGS_TAB)
    )

    # Нажимаем на вкладку
    fillings_tab.click()

    # Проверяем, что вкладка стала активной
    wait.until(
        lambda d: ACTIVE_TAB_CLASS in d.find_element(
            *FILLINGS_TAB
        ).get_attribute("class")
    )
