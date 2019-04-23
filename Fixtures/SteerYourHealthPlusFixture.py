# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture


class SteerYourHealthPlusFixture:

    def __init__(self, browser):
        target = r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for=\"UZSIP1-17\"]")))
        age17 = driver.find_element_by_css_selector("label[for=\"UZSIP1-17\"]")
        age17.click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btnBuy[btn-id=\"standart\"]")))
        time.sleep(5)
        standart = driver.find_element_by_css_selector("div.btnBuy[btn-id=\"standart\"]")
        standart.click()

    def insured_child(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[field-id=\"kidSection_surname\"]")))
        last_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_surname\"]")
        last_name.send_keys("Петрова")
        first_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_name\"]")
        first_name.send_keys("Елена")
        middle_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_secondName\"]")
        middle_name.send_keys("Петровна")
        dob = driver.find_element_by_css_selector("input[field-id=\"kidSection_birthdate\"]")
        dob.click()
        dob.send_keys("01012009"+Keys.ENTER)
        body = driver.find_element_by_tag_name("body")
        body.click()
        female = driver.find_element_by_css_selector("button[field-id=\"kidSection_female\"]")
        female.click()
        certificate = driver.find_element_by_css_selector("input[field-id=\"kidSection_birthCertificate\"]")
        certificate.click()
        certificate.send_keys("111111222222")
        issue_date = driver.find_element_by_css_selector("input[field-id=\"kidSection_issueDate\"]")
        issue_date.click()
        issue_date.send_keys("01012012" + Keys.ENTER)
        issue_organ = driver.find_element_by_css_selector("input[field-id=\"kidSection_issueOrgan\"]")
        issue_organ.send_keys("ОВД")
        button_next = driver.find_element_by_css_selector("button[data-next=\"step3\"]")
        button_next.click()

    def fill_frame(self):
        self.conditions()
        self.insured_child()
