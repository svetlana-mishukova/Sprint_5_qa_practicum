import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *
from helper import generate_registration_data

class TestLogout:
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
    def test_from_your_personal_account_to_the_designer(self, driver, registration_data): #авторизация и переход из личного кабинета в конструктор
        _, email, password = registration_data
        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее
        driver.find_element(*Locators.OUT_1).click() #находим элемент Личный кабинет и кликаем на нее
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.OUT_2))).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.OUT_3)))
    
        login_button_text = driver.find_element(*Locators.OUT_3).text
        assert login_button_text == "Войти"