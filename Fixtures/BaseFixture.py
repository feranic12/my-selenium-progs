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
            self.driver = webdriver.Firefox(firefox_binary=self.firefox_binary_path, executable_path=self.geckodriver_path)

    def open_page(self):
        self.driver.get(self.target)

    def pay_online(self):
        driver = self.driver
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "ccnumber")))
        time.sleep(5)
        ccnumber = driver.find_element_by_id("ccnumber")
        ccnumber.click()
        ccnumber.send_keys("4111111111111111")

    def destroy(self):
        self.driver.quit()