import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *
from data import invalid_password_data


class TestFailedRegistration:
    @pytest.mark.parametrize("name, email, password", invalid_password_data) 
    def test_failed_registration(self, driver, name, email, password): #проверка на ошибку для некорректного пароля
        driver.find_element(*Locators.LOGIN_BUTTON).click()  #находим кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него
        
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()  #находим кнопку Зарегистрироваться и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ERROR_M)) 
    
        assert driver.find_element(*Locators.PASSWORD).is_enabled(), f"Ошибка при проверке регистрации: поле пароля стало неактивным"
    
 
        assert not driver.current_url.endswith('/profile'), f"Ошибка при проверке регистрации: произошла неожиданная переадресация"