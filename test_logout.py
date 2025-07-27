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
    driver.find_element(*Locators.EMAIL).send_keys("Takayy@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASSWORD).send_keys("567488")  #вводим данные для поля Пароль
    driver.find_element(*Locators.REG_BUTTON).click() #находим кнопку Зарегистрироваться и кликаем на нее


def test_from_your_personal_account_to_the_designer(driver): #авторизация и переход из личного кабинета в конструктор
    driver.find_element(*Locators.LOGIN_BUTTON).click() #находим кнопку "Войти в аккаунт" и кликаем на нее
   
    driver.find_element(*Locators.EMAIL_AUTH).send_keys("Takayy@ya.ru") #вводим данные для поля email
    driver.find_element(*Locators.PASS_AUTH).send_keys("567488")  #вводим данные для поля Пароль
    driver.find_element(*Locators.BUTTON).click() #находим кнопку Войти и кликаем на нее
    driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']").click() #находим элемент Личный кабинет и кликаем на нее
    ebDriverWait(driver, 10).until(xpected_conditions.presence_of_element_located((By.XPATH, "//button [text()='Выход']"))).click()

    WebDriverWait(driver, 10).until(xpected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Войти']")))
    
    login_button_text = driver.find_element(By.XPATH, "//button[text()='Войти']").text
    assert login_button_text == "Войти"