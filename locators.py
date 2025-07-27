from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'a[href="/register"]')

    NAME = (By.CSS_SELECTOR, "fieldset:nth-child(1) input.text_type_main-default")
    EMAIL = (By.CSS_SELECTOR, "fieldset:nth-child(2) input.text_type_main-default")
    PASSWORD = (By.NAME, "Пароль")
    REG_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")

    LOGIN = (By.LINK_TEXT, "Войти")

    # Локаторы для авторизации
    EMAIL_AUTH = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    PASS_AUTH = (By.NAME, "Пароль")
    BUTTON = (By.XPATH, "//button[text()='Войти']")
    DES_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")