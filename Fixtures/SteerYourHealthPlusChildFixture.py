# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture


class SteerYourHealthPlusChildFixture(BaseFixture):

    def __init__(self, browser, target):
        BaseFixture.__init__(self, browser, target)
        self.action = ActionChains(self.driver)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for=\"UZSIP1-17\"]")))
        age17 = driver.find_element_by_css_selector("label[for=\"UZSIP1-17\"]")
        age17.click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btnBuy[btn-id=\"standart\"]")))
        time.sleep(4)
        standart = driver.find_element_by_css_selector("div.btnBuy[btn-id=\"standart\"]")
        standart.click()

    def insured_child(self):
        driver = self.driver
        action = self.action
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[field-id=\"kidSection_surname\"]")))
        last_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_surname\"]")
        last_name.send_keys("Петрова")
        first_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_name\"]")
        first_name.send_keys("Елена")
        middle_name = driver.find_element_by_css_selector("input[field-id=\"kidSection_secondName\"]")
        middle_name.send_keys("Петровна")
        dob = driver.find_element_by_css_selector("input[field-id=\"kidSection_birthdate\"]")
        dob.click()
        dob.send_keys("01012009" + Keys.ENTER)
        action.move_by_offset(200, 10).click().perform()
        female = driver.find_element_by_css_selector("button[field-id=\"kidSection_female\"]")
        female.click()
        certificate = driver.find_element_by_css_selector("input[field-id=\"kidSection_birthCertificate\"]")
        certificate.click()
        certificate.send_keys("111111222222")
        issue_date = driver.find_element_by_css_selector("input[field-id=\"kidSection_issueDate\"]")
        issue_date.click()
        issue_date.send_keys("01012012" + Keys.ENTER)
        action.move_by_offset(100, 10).click().perform()
        issue_organ = driver.find_element_by_css_selector("input[field-id=\"kidSection_issueOrgan\"]")
        issue_organ.send_keys("ОВД")
        button_next = driver.find_element_by_css_selector("button[data-next=\"step3\"]")
        button_next.click()

    def insurer_info(self):
        driver = self.driver
        action = self.action
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[field-id=\"insurerAdultSection_surname\"]")))
        last_name = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_surname\"]")
        last_name.send_keys("Петров")
        first_name = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_name\"]")
        first_name.send_keys("Пётр")
        middle_name = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_secondName\"]")
        middle_name.send_keys("Петрович")
        dob = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_birthdate\"]")
        dob.click()
        dob.send_keys("01011990"+Keys.ENTER)
        action.move_by_offset(100, 10).click().perform()
        male = driver.find_element_by_css_selector("button[field-id=\"insurerAdultSection_male\"]")
        male.click()
        passport = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_passportNumber\"]")
        passport.click()
        passport.send_keys("111111222222")
        issue_date = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_issueDate\"]")
        issue_date.click()
        issue_date.send_keys("01012012")
        #action.move_by_offset(-10, 20).click().perform()
        issue_organ = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_issueOrgan\"]")
        issue_organ.send_keys("ОВД")
        phone = driver.find_element_by_css_selector("input[field-id=\"insurerAdultSection_mobile\"]")
        phone.click()
        phone.send_keys("1231231212")
        list = driver.find_elements_by_css_selector("input[field-id=\"insurerAdultSection_email\"]")
        email = list[0]
        email.send_keys("knikitin@avinfors.ru")
        email1 = list[1]
        email1.send_keys("knikitin@avinfors.ru")
        button_next = driver.find_element_by_css_selector("button[data-next=\"step5\"]")
        button_next.click()

    def agree(self):
        driver = self.driver
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#checkboxBlock>div")))
        time.sleep(1)
        agree = driver.find_element_by_css_selector("div#checkboxBlock>div")
        agree.click()

    def to_payment(self):
        driver = self.driver
        visa_pay = driver.find_element_by_css_selector("div[code=\"72b8fcfa-de93-4f5b-993f-75b54d4254b2\"]")
        visa_pay.click()
        pay_button = driver.find_element_by_css_selector("button[data-paybutton]")
        pay_button.click()

    def fill_frame(self):
        self.conditions()
        self.insured_child()
        self.insurer_info()
        self.agree()
        #self.to_payment()
        #self.pay_online()