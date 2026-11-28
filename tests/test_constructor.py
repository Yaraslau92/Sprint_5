from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
    ACTIVE_TAB_CLASS
)
from urls import BASE_URL


class TestConstructor:

    # Проверка переключения на вкладку «Булки»
    def test_switch_to_buns(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 30)

        buns_tab = wait.until(
            EC.visibility_of_element_located(BUNS_TAB)
        )

        if ACTIVE_TAB_CLASS not in buns_tab.get_attribute("class"):
            wait.until(
                EC.element_to_be_clickable(BUNS_TAB)
            ).click()

        assert wait.until(
            lambda d: ACTIVE_TAB_CLASS in d.find_element(
                *BUNS_TAB
            ).get_attribute("class")
        )

    # Проверка переключения на вкладку «Соусы»
    def test_switch_to_sauces(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 30)

        wait.until(
            EC.element_to_be_clickable(SAUCES_TAB)
        ).click()

        assert wait.until(
            lambda d: ACTIVE_TAB_CLASS in d.find_element(
                *SAUCES_TAB
            ).get_attribute("class")
        )

    # Проверка переключения на вкладку «Начинки»
    def test_switch_to_fillings(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 30)

        wait.until(
            EC.element_to_be_clickable(FILLINGS_TAB)
        ).click()

        assert wait.until(
            lambda d: ACTIVE_TAB_CLASS in d.find_element(
                *FILLINGS_TAB
            ).get_attribute("class")
        )