import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *

def test_registration(driver):#регистрация
    driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
    driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него

    driver.find_element(*Locators.NAME).send_keys("Таня") #вводим данные для поля Имя
    driver.find_element(*Locators.EMAIL).send_keys("Taka@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASSWORD).send_keys("123321")  #вводим данные для поля Пароль
    driver.find_element(*Locators.REG_BUTTON).click() #находим кнопку Зарегистрироваться и кликаем на нее


def test_login_to_your_account(driver): #вход по кнопке «Войти в аккаунт» на главной 
    driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
    driver.find_element(*Locators.EMAIL_AUTH).send_keys("Taka@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASS_AUTH).send_keys("123321")  #вводим данные для поля Пароль
    driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

    text = driver.find_element(*Locators.DES_ORDER).text
    assert text == "Оформить заказ" 


def test_personal_account(driver):#вход через кнопку «Личный кабинет»
    driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']").click() #находим элемент Личный кабинет и кликаем на нее

    driver.find_element(*Locators.EMAIL_AUTH).send_keys("Taka@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASS_AUTH).send_keys("123321")  #вводим данные для поля Пароль
    driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

    text = driver.find_element(*Locators.DES_ORDER).text
    assert text == "Оформить заказ" 


def test_in_the_registration_form(driver): #вход через кнопку в форме регистрации
    driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
    driver.find_element(*Locators.REGISTER_BUTTON).click()  #находим элемент Зарегистрироваться и кликаем на него

    driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']").click() #находим элемент Войти и кликаем на него
    
    driver.find_element(By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default").send_keys("Taka@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASS_AUTH).send_keys("123321")  #вводим данные для поля Пароль
    driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

    text = driver.find_element(*Locators.DES_ORDER).text
    assert text == "Оформить заказ"     


def test_in_the_password_recovery_form(driver): #вход через кнопку в форме восстановления пароля
    driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
    
    driver.find_element(By.CSS_SELECTOR, "a[href='/forgot-password']").click() #находим элемент Восстановить пароль и кликаем на него
    driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']").click() #находим элемент Войти и кликаем на него

    driver.find_element(By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default").send_keys("Taka@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASS_AUTH).send_keys("123321")  #вводим данные для поля Пароль
    driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.DES_ORDER))

    text = driver.find_element(*Locators.DES_ORDER).text
    assert text == "Оформить заказ"  