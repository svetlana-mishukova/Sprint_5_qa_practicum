import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Locators
from curl import MAIN_PAGE

MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()