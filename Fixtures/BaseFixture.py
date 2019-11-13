from config import chromedriver_path, geckodriver_path, firefox_binary_path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class BaseFixture:

    def __init__(self, browser, target):
        self.chromedriver_path = chromedriver_path
        self.geckodriver_path = geckodriver_path
        self.firefox_binary_path = firefox_binary_path
        self.browser = browser
        self.target = target
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=self.chromedriver_path)
        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=self.geckodriver_path)

    def open_page(self):
        self.driver.get(self.target)

    def destroy(self):
        self.driver.quit()