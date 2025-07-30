from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'a[href="/register"]')

    NAME = (By.CSS_SELECTOR, "fieldset:nth-child(1) input.text_type_main-default")
    EMAIL = (By.CSS_SELECTOR, "fieldset:nth-child(2) input.text_type_main-default")
    PASSWORD = (By.NAME, "Пароль")
    REG_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    ERROR_M = (By.CSS_SELECTOR, "p.input__error.text_type_main-default")

    LOGIN = (By.LINK_TEXT, "Войти")

    # Локаторы для авторизации
    EMAIL_AUTH = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    PASS_AUTH = (By.NAME, "Пароль")
    BUTTON = (By.XPATH, "//button[text()='Войти']")
    DES_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ACCOUNT = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    FORM_1 = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")
    FORM_2 = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    FORM_PASS_1 = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    FORM_PASS_2 = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")
    FORM_PASS_3 = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")

    # Локаторы для Разделов
    SAUCE_1 = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Соусы']")
    SAUCE_2 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    FILLING_1 = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Начинки']")
    FILLING_2 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
    BUNS_1 = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Булки']")
    BUNS_2 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")

    # Локаторы для Конструктор
    CONSTR_1 = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    CONSTR_2 = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    CONSTR_3 = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")

    # Локаторы для перехода в ЛК
    PER_ACC_1 = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX')]/p[text()='Личный Кабинет']/..")
    PER_ACC_2 = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")

    #Локаторы для логотипа
    LOGO_1 = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX')]/p[text()='Личный Кабинет']/..")
    LOGO_2 = (By.CLASS_NAME , "AppHeader_header__logo__2D0X2")
    LOGO_3 = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")

    # Локаторы для выход из ЛК
    OUT_1 = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    OUT_2 = (By.XPATH, "//button [text()='Выход']")
    OUT_3 = (By.XPATH, "//button[text()='Войти']")
