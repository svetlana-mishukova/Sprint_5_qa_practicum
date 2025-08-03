import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from curl import *

class TestSectionConstructor:
    def test_section_of_sauce(self, driver):  
        driver.find_element(*Locators.SAUCE).click()  
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACTIVE_TAB_SAUCE))
        assert "Соусы" in active_tab.text
      
                  
    def test_section_of_filling(self, driver):  
        driver.find_element(*Locators.FILLING).click()
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACTIVE_TAB_FILLING))
        assert "Начинки" in active_tab.text
        

    def test_section_of_buns(self, driver):  
        driver.find_element(*Locators.BUNS).click()
        active_tab = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACTIVE_TAB_BUNS))
        assert "Булки" in active_tab.text
       