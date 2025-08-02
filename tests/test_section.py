import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import *

class TestSectionConstructor:
    def test_section_of_sauce(self, driver): #проверяем, что работают переходы к разделу Соусы
        driver.find_element(*Locators.SAUCE_1).click() #находим элемент Конструктов на странице и кликаем на него
        driver.find_element(*Locators.SAUCE_2).click() #находим и нажимаем раздел Булки
          
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((*Locators.SAUCE_3)))

        element = driver.find_element(*Locators.SAUCE_3)
        assert element.is_displayed(), "Раздел Соусы не отображается на странице"

        location = element.location
        rect = element.rect
        window_size = driver.get_window_size()
        
        assert location['y'] >= 0, "Элемент находится выше видимой области"
        assert location['y'] + rect['height'] <= window_size['height'], "Элемент находится ниже видимой области"


    def test_section_of_filling(self, driver): #проверяем, что работают переходы к разделу Начинки
        driver.find_element(*Locators.FILLING_1).click() #находим элемент Конструктов на странице и кликаем на него
        driver.find_element(*Locators.FILLING_2).click() 
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((*Locators.FILLING_3)))

        element = driver.find_element(*Locators.FILLING_3)
        assert element.is_displayed(), "Раздел Начинки не отображается на странице"

        location = element.location
        rect = element.rect
        window_size = driver.get_window_size()
        
        assert location['y'] >= 0, "Элемент находится выше видимой области"
        assert location['y'] + rect['height'] <= window_size['height'], "Элемент находится ниже видимой области"


    def test_section_of_buns(self, driver): #проверяем, что работают переходы к разделу Булки
        driver.find_element(*Locators.BUNS_1).click() #находим элемент Конструктов на странице и кликаем на него
        driver.find_element(*Locators.BUNS_2).click() 
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((*Locators.BUNS_3)))

        element = driver.find_element(*Locators.BUNS_3)
        assert element.is_displayed(), "Раздел Булки не отображается на странице"

        location = element.location
        rect = element.rect
        window_size = driver.get_window_size()
        
        assert location['y'] >= 0, "Элемент находится выше видимой области"
        assert location['y'] + rect['height'] <= window_size['height'], "Элемент находится ниже видимой области"