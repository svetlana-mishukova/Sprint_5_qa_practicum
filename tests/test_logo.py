import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *
from helper import generate_registration_data

class TestLogo:
    
    @pytest.mark.order(1)
    def test_registration(self, driver, registration_data):#регистрация
        name, email, password = registration_data
        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него

        driver.find_element(*Locators.NAME).send_keys(name) #вводим данные для поля Имя
        driver.find_element(*Locators.EMAIL).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASSWORD).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.REG_BUTTON).click() #находим кнопку Зарегистрироваться и кликаем на нее

    @pytest.mark.order(2)
    def test_login_to_your_account(self, driver, registration_data): #вход по кнопке «Войти в аккаунт» на главной 
        _, email, password = registration_data
        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        driver.find_element(*Locators.LOGO_1).click()

        driver.find_element(*Locators.LOGO_2).click()
    

        text = driver.find_element(*Locators.LOGO_3).text
        assert text == "Оформить заказ"