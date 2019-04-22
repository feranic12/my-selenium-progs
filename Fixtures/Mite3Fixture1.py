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
import pyperclip

class Mite3Fixture1(BaseFixture):

    def __init__(self, browser):
        target = r"https://testpartner.vtbins.ru/b2c/mite3/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        insured1_dob = driver.find_element_by_css_selector("div#calculation input[name=\"dob\"]")
        insured1_dob.click()
        insured1_dob.send_keys("11011990")
        _3months = driver.find_element_by_css_selector("button[data-code=\"3\"]")
        _3months.click()
        organization = driver.find_element_by_id("btn-med")
        organization.click()
        button_next = driver.find_element_by_css_selector("div#calculation button.btn-next")
        button_next.click()

    def insured1_info(self):
        driver = self.driver
        last_name = driver.find_element_by_css_selector("div#insuredPersons input[name=\"lastName\"]")
        last_name.send_keys("Иванов")
        first_name = driver.find_element_by_css_selector("div#insuredPersons input[name=\"firstName\"]")
        first_name.send_keys("Иван")
        middle_name = driver.find_element_by_css_selector("div#insuredPersons input[name=\"middleName\"]")
        middle_name.send_keys("Иванович")
        button_no = driver.find_element_by_css_selector("button[data-code=\"2\"]")
        button_no.click()
        phone = driver.find_element_by_name("phone")
        phone.click()
        phone.send_keys("1231231212")
        button_next = driver.find_element_by_css_selector("div#insuredPersons button.btn-next")
        button_next.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#client input[name=\"lastName\"]")))
        last_name = driver.find_element_by_css_selector("div#client input[name=\"lastName\"]")
        last_name.send_keys("Иванов")
        first_name = driver.find_element_by_css_selector("div#client input[name=\"firstName\"]")
        first_name.send_keys("Иван")
        middle_name = driver.find_element_by_css_selector("div#client input[name=\"middleName\"]")
        middle_name.send_keys("Иванович")
        region = driver.find_element_by_css_selector("input#region_s")
        region.send_keys("Москва"+Keys.ENTER)
        street = driver.find_element_by_id("street")
        street.send_keys("Маяковского")
        house = driver.find_element_by_id("house")
        house.send_keys("1")
        corp = driver.find_element_by_id("corp")
        corp.send_keys("2")
        building = driver.find_element_by_id("building")
        building.send_keys("3")
        flat = driver.find_element_by_id("flat")
        flat.send_keys("4")
        dob = driver.find_element_by_css_selector("div#client input[name=\"dob\"]")

    def fill_frame(self):
        self.conditions()
        self.insured1_info()
        self.insurer_info()