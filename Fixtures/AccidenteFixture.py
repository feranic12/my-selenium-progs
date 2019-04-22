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


class AccidenteFixture(BaseFixture):

    def __init__(self, browser):
        target = "https://testpartner.vtbins.ru/b2c/accidente/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame(0)

    def first_page(self):
        driver = self.driver
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[value *= "3 месяца"]')))
        term_3 = driver.find_element_by_css_selector('div[value *= "3 месяца"]')
        term_3.click()
        sport = driver.find_element_by_css_selector('div[idname=\"yes\"]')
        sport.click()
        hospital = driver.find_element_by_xpath(
            "//div[@id=\"container-header\"]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]")
        hospital.click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.btn.btn-primary[code=\"0\"]")))
        buy = driver.find_element_by_css_selector("div.btn.btn-primary[code=\"0\"]")
        buy.click()

    def begin_date(self, days):
        driver = self.driver
        begin = driver.find_element_by_id("beginDate")
        begin.send_keys(get_begin_day(days)+Keys.ENTER)

    def child(self):
        driver = self.driver
        last_name = driver.find_elements_by_name("lastName")[0]
        first_name = driver.find_elements_by_name("firstName")[0]
        middle_name = driver.find_elements_by_name("middleName")[0]
        last_name.send_keys("Иванова")
        first_name.send_keys("Елена")
        middle_name.send_keys("Ивановна")
        sex_female = driver.find_elements_by_name("sex")[1]
        sex_female.click()
        birth_date = driver.find_element_by_css_selector("input[name=\"dobB\"]")
        birth_date.send_keys("01.01.2009"+Keys.ENTER)

    def insurer(self):
        driver = self.driver
        last_name = driver.find_elements_by_name("lastName")[1]
        first_name = driver.find_elements_by_name("firstName")[1]
        middle_name = driver.find_elements_by_name("middleName")[1]
        last_name.send_keys("Иванов")
        first_name.send_keys("Иван")
        middle_name.send_keys("Иванович")
        sex_male = driver.find_elements_by_name("sex")[2]
        sex_male.click()
        birth_date = driver.find_element_by_css_selector("input[name=\"dob\"]")
        birth_date.send_keys("01.01.1990" + Keys.ENTER)
        passport_seria = driver.find_element_by_id("passportSeria")
        passport_seria.send_keys("1111")
        passport_number = driver.find_element_by_id("passportNumber")
        passport_number.send_keys("222222")
        passport_doi = driver.find_element_by_id("passportDoi")
        passport_doi.send_keys("01.03.2010"+Keys.ENTER)
        passport_issued = driver.find_element_by_id("passportIssued")
        passport_issued.send_keys("ОВД")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("+7(234)123-12-12")
        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")

    def flat_address(self):
        driver = self.driver
        region = driver.find_element_by_name("region")
        region.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value*=\"415\"]")))
        region_set = driver.find_element_by_css_selector("div[value*=\"415\"]")
        region_set.click()
        city = driver.find_element_by_name("cityA")
        city.send_keys("Москва")
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

    def agree(self):
        driver = self.driver
        agree = driver.find_element_by_name("agree")
        agree.click()

    def fill_frame(self):
        self.first_page()
        self.begin_date(10)
        self.child()
        self.insurer()
        self.flat_address()
        self.agree()