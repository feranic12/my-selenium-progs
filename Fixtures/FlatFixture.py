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

class FlatFixture(BaseFixture):

    def __init__(self,browser,target):
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        driver = self.driver
        driver.get(self.target)
        driver.switch_to.frame("RESOLUTE_INSURANCE")

    def is_frame_filled(self):
        return (self.driver.find_element_by_css_selector("img[src *=\"3B2441ED-482F-10E1-0E2D-1E6C86FD91F6.png\"]"))

    def first_page(self):
        driver = self.driver
        flat_area = driver.find_element_by_id("area")
        flat_area.send_keys("100")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value *= 'МО']")))
        mo=driver.find_element_by_css_selector("div[value *= 'МО']")
        mo.click()
        yes_private = driver.find_element_by_css_selector("div[name='privat'] div:first-child")
        yes_rent = driver.find_element_by_css_selector("div[name='rent'] div:first-child")
        yes_private.click()
        yes_rent.click()
        buy_standart = driver.find_element_by_css_selector("div#product-variant-1 div.btn-primary")
        buy_standart.click()

    def additional_block(self):
        driver = self.driver
        select_go = Select(driver.find_element_by_css_selector("select[register='pl_ss']"))
        select_go.select_by_index(1)
        select_strah = Select(driver.find_element_by_css_selector("select[register='ai_ss']"))
        select_strah.select_by_index(1)

    def begin_date(self,days):
        driver = self.driver
        begin_date = driver.find_element_by_id("beginDate")
        begin_date.send_keys(get_begin_day(days))
        begin_date.send_keys(Keys.ENTER)

    def flat_address(self):
        driver = self.driver
        region = driver.find_element_by_name("region")
        region.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value*=\"415\"]")))
        moscow = driver.find_element_by_css_selector("div[value*=\"415\"]")
        moscow.click()
        street = driver.find_element_by_name("street")
        street.send_keys("Маяковского")
        house = driver.find_element_by_name("house")
        house.send_keys("12")
        corp = driver.find_element_by_name("corp")
        corp.send_keys("3")
        building = driver.find_element_by_name("building")
        building.send_keys("4")
        flat = driver.find_element_by_name("flat")
        flat.send_keys("3")

    def insurer_info(self):
        driver = self.driver
        last_name = driver.find_element_by_name("lastName")
        last_name.send_keys("Петров")
        first_name = driver.find_element_by_name("firstName")
        first_name.send_keys("Пётр")
        middle_name = driver.find_element_by_name("middleName")
        middle_name.send_keys("Петрович")
        seria = driver.find_element_by_id("passportSeria")
        seria.send_keys("1234")
        number = driver.find_element_by_id("passportNumber")
        number.send_keys("123456")
        passport_date = driver.find_element_by_id("passportDoi")
        passport_date.send_keys("12102014")
        passport_date.send_keys(Keys.ENTER)
        issued = driver.find_element_by_name("passportIssued")
        issued.send_keys("ОВД")
        birthdate = driver.find_element_by_id("dobA")
        birthdate.send_keys("21101978")
        birthdate.send_keys(Keys.ENTER)
        phone = driver.find_element_by_name("phone")
        phone.send_keys("+7(234)123-12-12")
        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")

    def agree(self):
        driver = self.driver
        agree = driver.find_element_by_name("agree")
        agree.click()

    def fill_frame(self):
        driver = self.driver
        self.first_page()
        self.additional_block()
        self.begin_date(10)
        self.flat_address()
        self.insurer_info()
        self.agree()
