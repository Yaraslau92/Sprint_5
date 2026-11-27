
from selenium.webdriver.common.by import By


# Поля регистрации и входа
NAME_INPUT = (
    By.XPATH,
    "//label[normalize-space()='Имя']/following-sibling::input"
)

EMAIL_INPUT = (
    By.XPATH,
    "//label[normalize-space()='Email']/following-sibling::input"
)

PASSWORD_INPUT = (By.NAME, "Пароль")


# Кнопки регистрации и входа
REGISTER_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Зарегистрироваться']"
)

LOGIN_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Войти']"
)

LOGIN_FROM_HOME_BUTTON = (
    By.CSS_SELECTOR,
    "button.button_button__33qZ0"
)


# Ссылка на страницу входа
LOGIN_LINK = (
    By.CSS_SELECTOR,
    "a.Auth_link__1fOlj[href='/login']"
)


# Навигация
PERSONAL_ACCOUNT_LINK = (
    By.XPATH,
    "//a[@href='/account' and .//p[normalize-space()='Личный Кабинет']]"
)

CONSTRUCTOR_LINK = (
    By.CSS_SELECTOR,
    'a[href="/"]'
)

LOGO_LINK = (
    By.CSS_SELECTOR,
    ".AppHeader_header__logo__2D0X2 a"
)


# Вкладки конструктора
BUNS_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab__') and .//span[text()='Булки']]"
)

SAUCES_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab__') and .//span[text()='Соусы']]"
)

FILLINGS_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab__') and .//span[text()='Начинки']]"
)


# Класс активной вкладки
ACTIVE_TAB_CLASS = "tab_tab_type_current__2BEPc"
