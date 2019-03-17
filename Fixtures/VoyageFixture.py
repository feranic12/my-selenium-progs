# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime,timedelta
import time
from utils import get_begin_day
from configs import chromedriver_path


class VoyageFixture:

    def __init__(self,cmdopt):
        self.days = cmdopt
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.get("https://testpartner.vtbins.ru/b2c/voyage/test-main.html")
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")
        self.action=webdriver.common.action_chains.ActionChains(self.driver)

    def insured_birthdates(self):
        driver = self.driver
        body = driver.find_element_by_tag_name("body")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[_insured=\"1\"]>label:first-child")))
        insured1 = driver.find_element_by_css_selector("div[_insured=\"1\"]>label:first-child")
        insured1.click()
        insured1_dob = driver.find_element_by_css_selector("div[_insured=\"1\"]>label:nth-child(2)>input")
        insured1_dob.click()
        insured1_dob.send_keys("10021990")
        body.click()

    def trip_type(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div#tripType>label:nth-child(2)")))
        trip_type = driver.find_element_by_css_selector("label[code=\"single\"]")
        trip_type.click()

    def country_select(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "countries")))
        time.sleep(1)
        choose_country = driver.find_element_by_id("countries")
        choose_country.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value *= \"Шенген\"]")))
        schengen = driver.find_element_by_css_selector("div[value *= \"Шенген\"]")
        schengen.click()

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#meSS>label[code=\"50000\"]")))
        summa50000 = driver.find_element_by_css_selector("div#meSS>label[code=\"50000\"]")
        summa50000.click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"departures")))
        time.sleep(1)

    def trip_dates(self,days):
        action = self.action
        driver = self.driver
        begin_date = driver.find_element_by_name("departures")
        begin_date.click()
        begin_date.send_keys(get_begin_day(days))
        action.move_by_offset(100,100).click().perform()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "arrivals")))
        end_date=driver.find_element_by_name("arrivals")
        end_date.click()
        end_date.send_keys(get_begin_day(20))
        action.move_by_offset(100,100).click().perform()
        time.sleep(1)

    def buy(self):
        driver = self.driver
        not_needed = driver.find_element_by_css_selector("label[code=\"no\"][for=\"15\"]")
        not_needed.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "buy_econom")))
        buy_econom = driver.find_element_by_id("buy_econom")
        buy_econom.click()

    def continue_without(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addComplite")))
        continue_without = driver.find_element_by_id("addComplite")
        driver.execute_script("arguments[0].click();", continue_without)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[name=\"Insurer_1\"] input[name=\"lastName\"]")))

    def insured_info(self):
        driver = self.driver
        ins1_surname = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"lastName\"]")
        ins1_surname.click()
        ins1_surname.send_keys("Петров")
        ins1_firstname = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"firstName\"]")
        ins1_firstname.click()
        ins1_firstname.send_keys("Пётр")
        ins1_middlename = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"middleName\"]")
        ins1_middlename.click()
        ins1_middlename.send_keys("Петрович")
        ins1_eng_surname = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"surName\"]")
        ins1_eng_surname.click()
        ins1_eng_surname.send_keys("PETROV")
        ins1_eng_surname = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"givenNames\"]")
        ins1_eng_surname.click()
        ins1_eng_surname.send_keys("PETR")
        passport = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] input[name=\"passport\"]")
        passport.click()
        passport.send_keys("12 123456")
        is_insured_yes=driver.find_element_by_css_selector("div[name=\"Insurer_1\"] button[name=\"isInsuredOn")
        is_insured_yes.click()
        male = driver.find_element_by_css_selector("div[name=\"Insurer_1\"] button[data-value=\"male\"]")
        male.click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ("div.sectionInsurersButton>button"))))
        continue_button = driver.find_element_by_css_selector(("div.sectionInsurersButton>button"))
        continue_button.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "phone")))
        phone = driver.find_element_by_name("phone")
        phone.send_keys("1112223344")
        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")
        continue_button1 = driver.find_element_by_css_selector(("div.sectionConfirmButton>button"))
        continue_button1.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label.checkbox.final>span.checkbox-icon")))
        agree = driver.find_element_by_css_selector("label.checkbox.final>span.checkbox-icon")
        agree.click()

    def fill_frame(self):
        self.insured_birthdates()
        self.trip_type()
        self.country_select()
        self.conditions()
        self.trip_dates(self.days)
        self.buy()
        self.continue_without()
        self.insured_info()
        self.insurer_info()
        self.agree()

