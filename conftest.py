import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import MAIN_PAGE

from helper import generate_registration_data


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def registration_data():    
    return generate_registration_data()

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get(MAIN_PAGE)
    driver.delete_all_cookies()