from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture


class AccidenteFixture(BaseFixture):

    def __init__(self, browser):
        target = "https://testpartner.vtbins.ru/b2c/accidente/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        driver = self.driver
        driver.get(self.target)
        driver.switch_to.frame(0)

    def fill_frame(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[value *= "3 месяца"]')))
        term_3 = driver.find_element_by_css_selector('div[value *= "3 месяца"]')
        term_3.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn.btn-combobox[value=\"{\"code\":\"3\",\"name\":\"Да\"}\"]")))
        sport = driver.find_element_by_css_selector("div.btn.btn-combobox[value=\"{\"code\":\"3\",\"name\":\"Да\"}\"]")
        