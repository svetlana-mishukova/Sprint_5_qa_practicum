import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *


def test_section_of_sauce(driver): #проверяем, что работают переходы к разделу Соусы
    driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']").click() #находим элемент Конструктов на странице и кликаем на него
    driver.find_element(By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']").click() #находим и нажимаем раздел Булки
          
def is_element_scrolled_into_view(element): # проверяем позицию прокрутки до раздела Соусы
    return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return rect.top >= 0 && rect.bottom <= window.innerHeight;
    """, element)

    element = driver.find_element(By.CSS_SELECTOR, "Соусы")
    assert is_element_scrolled_into_view(element), "Элемент не прокрутился в видимую область"


def test_section_of_filling(driver): #проверяем, что работают переходы к разделу Начинки
    driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']").click() #находим элемент Конструктов на странице и кликаем на него
    driver.find_element(By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']").click() 
    
def is_element_scrolled_into_view(element): #проверяем позицию прокрутки до раздела Начинки
    return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return rect.top >= 0 && rect.bottom <= window.innerHeight;
    """, element)

    element = driver.find_element(By.CSS_SELECTOR, "Начинки")
    assert is_element_scrolled_into_view(element), "Элемент не прокрутился в видимую область"


def test_section_of_buns(driver): #проверяем, что работают переходы к разделу Булки
    driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']").click() #находим элемент Конструктов на странице и кликаем на него
    driver.find_element(By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']").click() 
    
def is_element_scrolled_into_view(element): # проверяем позицию прокрутки до раздела Булки
    return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return rect.top >= 0 && rect.bottom <= window.innerHeight;
    """, element)

    element = driver.find_element(By.CSS_SELECTOR, "Булки")
    assert is_element_scrolled_into_view(element), "Элемент не прокрутился в видимую область"