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
from config import chromedriver_path
from Fixtures.BaseFixture import BaseFixture


class MilitaryFixture:

    def __init__(self, browser):
        target = r"https://testpartner.vtbins.ru/b2c/military/test-main.html"
        BaseFixture.__init__(self,browser,target)

    def open_page(self):
        self.driver.get(self.target)
        self.driver.switch_to.frame(0)

    def choose_place(self):
        driver = self.driver
        choose_place = driver.find_elements_by_css_selector("div#calculation button")[0]
        choose_place.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-raw *= \"ВТБ (ПАО)\"]")))
        vtb24 = driver.find_element_by_css_selector("div[data-raw *= \"ВТБ (ПАО)\"]")
        vtb24.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-raw *= \"Москва\"]")))
        moscow = driver.find_element_by_css_selector("div[data-raw *= \"Москва\"]")
        moscow.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-raw *= \"Дмитровский\"]")))
        habarovsk = driver.find_element_by_css_selector("div[data-raw *= \"Дмитровский\"]")
        habarovsk.click()

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-path=\"content.contractData.flat.creditSize\"]")))
        credit = driver.find_element_by_css_selector("input[data-path=\"content.contractData.flat.creditSize\"]")
        credit.send_keys("100000")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-path=\"content.contractData.flat.rate\"]")))
        credit = driver.find_element_by_css_selector("input[data-path=\"content.contractData.flat.rate\"]")
        credit.send_keys("20")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-path=\"content.contractData.flat.countMonth\"]")))
        count_months = driver.find_element_by_css_selector("input[data-path=\"content.contractData.countMonth\"]")
        count_months.send_keys("30")
        buttons = driver.find_elements_by_class_name("sectionInsurersButton")
        buttons[0].click()
        buttons[1].click()

    def flat_address(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-path=\"content.object.address\"]")))
        address = driver.find_element_by_css_selector("input[data-path=\"content.object.address\"]")
        address.send_keys("Москва")
        time.sleep(1)
        address.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        address.send_keys(Keys.ENTER)
        address1 = driver.find_element_by_css_selector("input[data-path=\"content.object.street\"]")
        address1.send_keys("Маяковская 34 17")
        button_3 = driver.find_element_by_css_selector("button[data-for=\"step3\"]")
        button_3.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-path=\"content.insuredPerson.lastName\"]")))
        last_name = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.lastName\"]")
        last_name.send_keys("Петров")
        first_name = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.firstName\"]")
        first_name.send_keys("Пётр")
        middle_name = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.middleName\"]")
        middle_name.send_keys("Петрович")
        dob = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.dob\"]")
        dob.click()
        dob.send_keys("18021980")
        body = driver.find_element_by_tag_name("body")
        body.click()
        time.sleep(2)
        male = driver.find_element_by_css_selector("button[value*=\"Мужской\"]")
        male.click()
        passport = driver.find_element_by_css_selector("input[data-type=\"passport\"]")
        passport.click()
        passport.send_keys("1234 123456")
        doi = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.passport.doi\"]")
        doi.click()
        doi.send_keys("18022014")
        body.click()
        issued = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.passport.issued\"]")
        issued.send_keys("ОВД")
        phone = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.phone\"]")
        phone.click()
        phone.send_keys("1112223344")
        email1 = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.email\"]")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_css_selector("input[equal=\"content.insuredPerson.email\"]")
        email2.send_keys("knikitin@avinfors.ru")
        insurer_address = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.address\"]")
        insurer_address.send_keys("Москва")
        time.sleep(1)
        insurer_address.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        insurer_address.send_keys(Keys.ENTER)
        insurer_address1 = driver.find_element_by_css_selector("input[data-path=\"content.insuredPerson.street\"]")
        insurer_address1.send_keys("Маяковская 34 17")
        button_4 = driver.find_element_by_css_selector("button[data-for=\"step4\"]")
        button_4.click()

    def agree(self):
        driver = self.driver
        time.sleep(2)
        agree1 = driver.find_element_by_id("checkbox1")
        agree1.click()
        agree2 = driver.find_element_by_id("checkbox2")
        agree2.click()

    def fill_frame(self):
        driver = self.driver
        self.choose_place()
        self.conditions()
        self.flat_address()
        self.insurer_info()
        self.agree()