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
from configs import chromedriver_path


class MultipolicyFixture:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.get("https://testpartner.vtbins.ru/b2c/multipolicy/test-main.html")
        self.driver.switch_to.frame(0)

    def policy_info(self):
        driver=self.driver
        driver.find_element_by_name("number1").send_keys("33522")
        driver.find_element_by_name("activecode").send_keys("123456")

    def insurer(self):
        driver=self.driver
        driver.find_element_by_name("lastName").send_keys("Петров")
        driver.find_element_by_name("firstName").send_keys("Пётр")
        driver.find_element_by_name("middleName").send_keys("Петрович")
        driver.find_element_by_name("passportSeria").send_keys("1234")
        driver.find_element_by_name("passportNumber").send_keys("123456")
        driver.find_element_by_name("passportDoi").send_keys("04112015")
        driver.find_element_by_name("depCode").send_keys("123123")
        driver.find_element_by_name("passportIssued").send_keys("ОВД")
        driver.find_element_by_name("dobA").send_keys("01011980")
        driver.find_element_by_name("address").send_keys("Россия")
        driver.find_element_by_name("cityA").send_keys("Екатеринбург")
        driver.find_element_by_name("street").send_keys("Маяковского")
        driver.find_element_by_name("house").send_keys("12")
        driver.find_element_by_name("corp").send_keys("1")
        driver.find_element_by_name("building").send_keys("2")
        driver.find_element_by_name("flat").send_keys("83")
        driver.find_element_by_name("snils").send_keys("12345678901")
        driver.find_element_by_name("inn").send_keys("123456789012")
        driver.find_element_by_name("phone").send_keys("12345678901")
        driver.find_element_by_name("email1").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_name("email2").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_css_selector("div[value*=Мужской]").click()

    def fill_frame(self):
        self.policy_info()
        self.insurer()
