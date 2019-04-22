from config import chromedriver_path, geckodriver_path, firefox_binary_path
from selenium import webdriver


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