import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *
from helper import generate_registration_data

class TestLogin:
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

        driver.delete_all_cookies()
        driver.get(MAIN_PAGE)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

        text = driver.find_element(*Locators.DES_ORDER).text
        assert text == "Оформить заказ" 

    @pytest.mark.order(3)
    def test_personal_account(self, driver, registration_data):#вход через кнопку «Личный кабинет»
        _, email, password = registration_data

        driver.delete_all_cookies()
        driver.get(MAIN_PAGE) 

        driver.find_element(*Locators.ACCOUNT).click() #находим элемент Личный кабинет и кликаем на нее

        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

        text = driver.find_element(*Locators.DES_ORDER).text
        assert text == "Оформить заказ" 

    @pytest.mark.order(4)
    def test_in_the_registration_form(self, driver, registration_data): #вход через кнопку в форме регистрации
        _, email, password = registration_data

        driver.delete_all_cookies()
        driver.get(MAIN_PAGE)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него

        driver.find_element(*Locators.FORM_1).click() #находим элемент Войти и кликаем на него
    
        driver.find_element(*Locators.FORM_2).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

        text = driver.find_element(*Locators.DES_ORDER).text
        assert text == "Оформить заказ"     

    @pytest.mark.order(5)
    def test_in_the_password_recovery_form(self, driver, registration_data): #вход через кнопку в форме восстановления пароля
        _, email, password = registration_data

        driver.delete_all_cookies()
        driver.get(MAIN_PAGE)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
    
        driver.find_element(*Locators.FORM_PASS_1).click() #находим элемент Восстановить пароль и кликаем на него
        driver.find_element(*Locators.FORM_PASS_2).click() #находим элемент Войти и кликаем на него

        driver.find_element(*Locators.FORM_PASS_3).send_keys(email) #вводим данные для поля email
        driver.find_element(*Locators.PASS_AUTH).send_keys(password)  #вводим данные для поля Пароль
        driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

        text = driver.find_element(*Locators.DES_ORDER).text
        assert text == "Оформить заказ"  