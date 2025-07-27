import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *

invalid_password_data = [
    ("Иван", "Ivanov_Ivan@ya.ru", "123"),
    ("Иван", "Ivanov_Ivan@ya.ru", "12345"),
    ]

@pytest.mark.parametrize("name, email, password", invalid_password_data) 
def test_successful_registration(driver, name, email, password): #проверка на ошибку для некорректного пароля
    try:
        driver.find_element(*Locators.LOGIN_BUTTON).click()  #находим кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него
        
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()  #находим кнопку Зарегистрироваться и кликаем на нее


        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.input__error.text_type_main-default")))
    
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"
        
        driver.find_element(By.LINK_TEXT, "Войти")

    except Exception as e:
        pytest.fail(f"Ошибка при проверке регистрации: {str(e)}")