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


class MedOnlineFixture(BaseFixture):#программа МедОнлайн6

    def __init__(self, browser):
        target = "https://testpartner.vtbins.ru/b2c/sip/build/test-medOnlineSIP.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.col-md-5 button:nth-child(2)")))
        age18 = driver.find_element_by_css_selector("div.col-md-5 button:nth-child(2)")
        age18.click()
        distance_1 = driver.find_element_by_css_selector("div#distance-table tr#distance-buttons>td:nth-child(2)>button")
        distance_1.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div#organize-table tr#organize-table-buttons>td:nth-child(3)>button")))
        organize_2 = driver.find_element_by_css_selector("div#organize-table tr#organize-table-buttons>td:nth-child(3)>button")
        organize_2.click()

    def insurer(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder=\"Фамилия\"]")))
        last_name = driver.find_element_by_css_selector("input[placeholder=\"Фамилия\"]")
        last_name.send_keys("Петров")
        first_name = driver.find_element_by_css_selector("input[placeholder=\"Имя\"]")
        first_name.send_keys("Пётр")
        middle_name = driver.find_element_by_css_selector("input[placeholder=\"Отчество\"]")
        middle_name.send_keys("Петрович")
        dob = driver.find_element_by_id("content.policyHolder.dob")
        dob.click()
        dob.send_keys("01011990")
        male = driver.find_element_by_css_selector("div[role=group]>button:first-child")
        male.click()
        phone = driver.find_element_by_id("content.policyHolder.phone")
        phone.click()
        phone.send_keys("1231231212")
        email = driver.find_element_by_css_selector("input[placeholder=\"E-mail\"]")
        email.send_keys("knikitin@avinfors.ru")
        email1 = driver.find_element_by_css_selector("input[placeholder=\"Подтвердите e-mail\"]")
        email1.send_keys("knikitin@avinfors.ru")
        button_next = driver.find_element_by_css_selector("button[type=\"submit\"]")
        button_next.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "properties.agreement")))
        agree = driver.find_element_by_css_selector("label.c01101>div")
        agree.click()

    def fill_frame(self):
        self.conditions()
        self.insurer()
        self.agree()