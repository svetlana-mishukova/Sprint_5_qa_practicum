import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *
from helper import generate_registration_data


class TestPersonalAccount:
    
    def test_registration(self, driver, registration_data):#регистрация
        name, email, password = registration_data
        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него

        driver.find_element(*Locators.NAME).send_keys(name) #вводим данные для поля Имя
        driver.find_element(*Locators.EMAIL).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASSWORD).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.REG_BUTTON).click() #находим кнопку Зарегистрироваться и кликаем на нее
        login_text = driver.find_element(*Locators.LOGIN).text
        assert login_text == "Войти"


    def test_login_to_your_account(self, driver, registration_data): #авторизация и переход по клику на «Личный кабинет»
        _, email, password = registration_data
        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((Locators.PER_ACC_1))).click()

        button_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Locators.PER_ACC_2))).text
        assert button_text == "Сохранить"