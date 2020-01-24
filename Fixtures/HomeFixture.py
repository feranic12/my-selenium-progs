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


class HomeFixture(BaseFixture):

    def __init__(self,browser):
        target = r"https://testpartner.vtbins.ru/b2c/insuranceHomeMoscow/test-main.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)

    def address(self):
        driver = self.driver
        time.sleep(5)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id=\"districtButtonSet\"]/table//tr/td[2]")))
        south_district = driver.find_element_by_xpath(("//div[@id=\"districtButtonSet\"]//tr/td[2]"))
        south_district.click()
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "streetSelect")))
        #street_select = driver.find_element_by_id("streetSelect")
        #street_select.click()
        #street_select.send_keys(Keys.ARROW_DOWN+Keys.ENTER)

    def fill_frame(self):
        self.address()

