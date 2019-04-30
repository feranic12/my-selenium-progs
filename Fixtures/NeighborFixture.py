# -*- coding: utf-8 -*-
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


class NeighborFixture(BaseFixture):

    def __init__(self,browser):
        target = "https://testpartner.vtbins.ru/b2c/neighbor/"
        BaseFixture.__init__(self, browser, target)

    def policy_data(self):
        driver = self.driver
        active_code = driver.find_element_by_name("activecode")
        active_code.send_keys("123456")

    def insurer_info(self):
        driver = self.driver
        radio_female = driver.find_elements_by_css_selector("label.radio.span2>span:first-child")[0]
        radio_female.click()
        last_name = driver.find_element_by_name("lastName")
        last_name.send_keys("Петрова")
        first_name = driver.find_element_by_name("firstName")
        first_name.send_keys("Елена")
        middle_name = driver.find_element_by_name("middleName")
        middle_name.send_keys("Петровна")
        dob = driver.find_element_by_name("dob")
        dob.click()
        dob.send_keys("01011990"+Keys.ENTER)
        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")
        phone = driver.find_element_by_name("phone")
        phone.click()
        phone.send_keys("1231231212")

    def flat_address(self):
        driver = self.driver
        radio_flat = driver.find_elements_by_css_selector("label.radio.span3>span:first-child")[1]
        radio_flat.click()
        region = driver.find_element_by_id("region_chzn")
        region.click()
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.chzn-results>li:nth-child(2)")))
        moscow = driver.find_element_by_css_selector("ul.chzn-results>li:nth-child(2)")
        moscow.click()
        city = driver.find_element_by_name("city")
        city.send_keys("Москва")
        street = driver.find_element_by_name("street")
        street.send_keys("Маяковского")
        house = driver.find_element_by_name("house")
        house.send_keys("34")
        corp = driver.find_element_by_name("corp")
        corp.send_keys("1")
        building = driver.find_element_by_name("building")
        building.send_keys("2")
        flat = driver.find_element_by_name("flat")
        flat.send_keys("3")

    def agree(self):
        driver = self.driver
        agree = driver.find_element_by_css_selector("span.niceCheck.toRight")
        agree.click()

    def fill_frame(self):
        self.policy_data()
        self.insurer_info()
        self.flat_address()
        self.agree()
