# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time, pyperclip
from utils import get_begin_day
from config import chromedriver_path
from Fixtures.BaseFixture import BaseFixture


class SteerYourHealthPlusFixture:

    def __init__(self, browser):
        target = r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html"
        BaseFixture.__init__(self, browser, target)
        self.actions = action_chains.ActionChains(self.driver)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def fill_frame(self):
        driver=self.driver
        actions=self.actions
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id=UZSIP18-50]")))
        driver.find_element_by_css_selector("label[for=UZSIP18-50]").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[btn-id=\"econom\"]")))
        driver.find_element_by_css_selector("div[btn-id=\"econom\"]").click()
        a="var surname_field=document.querySelector('div[btn-id=\"econom\"]');"