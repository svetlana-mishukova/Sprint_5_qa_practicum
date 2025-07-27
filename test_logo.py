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

    driver.find_element(By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX')]/p[text()='Личный Кабинет']/..").click()

    driver.find_element(By.CLASS_NAME , "AppHeader_header__logo__2D0X2").click()


    text = driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg").text
    assert text == "Оформить заказ"