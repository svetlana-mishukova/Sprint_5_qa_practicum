import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *

registration_data = [
    ("Иван", "Ivanov_Ivan@ya.ru", "123456"),
    ("Анна", "Anna_111@yandex.ru", "567345"),
] 

@pytest.mark.parametrize("name, email, password", registration_data)
def test_successful_registration(driver, name, email, password): # проверка на успешную регистрацию
    driver.find_element(*Locators.LOGIN_BUTTON).click()  #находим кнопку "Войти в аккаунт" и кликаем на нее
    driver.find_element(*Locators.REGISTER_BUTTON).click() #находим элемент Зарегистрироваться и кликаем на него
    
    driver.find_element(*Locators.NAME).send_keys(name)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(password)

    driver.find_element(*Locators.REG_BUTTON).click() #находим кнопку Зарегистрироваться и кликаем на нее

    login_text = driver.find_element(*Locators.LOGIN).text
    assert login_text == "Войти"