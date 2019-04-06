# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from config import chromedriver_path
from utils import get_begin_day
import pyperclip
from Fixtures.BaseFixture import BaseFixture


class VhiVzrFixture():

    def __init__(self):
        target = r"https://testpartner.vtbins.ru/b2c/vhi/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        driver = self.driver
        driver.get(self.target)
        driver.switch_to.frame(0)

    def fill_frame(self):
        driver = self.driver

        first_number=driver.find_element_by_name("policyNumber1")
        first_number.send_keys("01050100")

        second_number = driver.find_element_by_name("policyNumber2")
        second_number.send_keys("04377")

        third_number = driver.find_element_by_name("policyNumber3")
        third_number.send_keys("0044")

        last_name=driver.find_element_by_name("lastName")
        last_name.send_keys("Дей")

        first_name = driver.find_element_by_name("firstName")
        pyperclip.copy("FirstName110799")
        first_name.send_keys(Keys.LEFT_CONTROL+"v")

        middle_name = driver.find_element_by_name("middleName")
        pyperclip.copy("SecondName110799")
        middle_name.send_keys(Keys.LEFT_CONTROL+"v")

        check_button=driver.find_element_by_name("next-1")
        check_button.click()

        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id=\"container-header\"]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]")))
        find_button=driver.find_element_by_xpath("//div[@id=\"container-header\"]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[1]")
        find_button.click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value *= \"США\"]")))
        usa = driver.find_element_by_css_selector("div[value *= \"США\"]")
        usa.click()

        time.sleep(5)
        summa100000 = driver.find_element_by_xpath("//div[@id=\"container-header\"]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div[1]/div[5]")
        summa100000.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div#product-variant-2 div.btn-primary")))
        buy_button = driver.find_element_by_css_selector("div#product-variant-2 div.btn-primary")
        buy_button.click()

        begin_date = driver.find_element_by_id("beginDate")
        begin_date.send_keys(get_begin_day(6)+Keys.ENTER)

        surname = driver.find_element_by_name("Surname")
        surname.send_keys("Malinin")

        given_name = driver.find_element_by_name("Given names")
        given_name.send_keys("Vjacheslav")

        passport = driver.find_element_by_id("passport")
        passport.send_keys("12 123456")

        phone = driver.find_element_by_name("phone")
        phone.send_keys("7777777777")

        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")

        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")

        agree = driver.find_element_by_name("agree")
        agree.click()


