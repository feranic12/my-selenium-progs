from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from utils import get_begin_day
from configs import chromedriver_path


class Travel():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.get("https://testpartner.vtbins.ru/b2c/travel/test-main.html")
        self.driver.switch_to.frame(0)
        self.fill_frame()

    def first_page(self):
        driver=self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value*=\"Однократная\"]")))
        single = driver.find_element_by_css_selector("div[value*=\"Однократная\"]")
        single.click()
        find_country = driver.find_element_by_css_selector("div.btn.btn-primary.multi-select[register='countries']")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn.btn-primary.multi-select[register='countries']")))
        find_country.click()
        shenghen = driver.find_element(By.CSS_SELECTOR, "div[value *= \"Шенген\"]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[value *= \"Шенген\"")))
        shenghen.click()
        trip_term = driver.find_element(By.ID, "tripTerm")
        trip_term.send_keys("15")
        age = driver.find_element(By.ID, "age")
        age.send_keys("36")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[register=\"sport\"]>div[value *= \"Нет\"]")))
        sport = driver.find_element_by_css_selector("div[register=\"sport\"]>div[value *= \"Нет\"]")
        driver.execute_script("arguments[0].click()", sport)
        buy_button = driver.find_element_by_css_selector("div[code=\"econom\"]")
        driver.execute_script("arguments[0].click()", buy_button)

    def begin_date(self,days):
        driver=self.driver
        begin_date = driver.find_element_by_id("beginDate")
        begin_date.send_keys(get_begin_day(days))

    def insurer_info(self):
        driver=self.driver
        last_name = driver.find_element_by_name("lastName")
        last_name.send_keys("Петров")
        first_name = driver.find_element_by_name("firstName")
        first_name.send_keys("Пётр")
        middle_name = driver.find_element_by_name("middleName")
        middle_name.send_keys("Петрович")
        eng_last_name = driver.find_element_by_css_selector("input#fld-001-cmp[name=\"Surname\"]")
        eng_last_name.send_keys("Petrov")
        eng_first_name = driver.find_element_by_css_selector("input#fld-001-cmp[name=\"Given names\"]")
        eng_first_name.send_keys("Petr")
        birthdate = driver.find_element_by_id("dobA")
        birthdate.send_keys("10101980")
        birthdate.send_keys(Keys.ENTER)
        seria_number = driver.find_element_by_id("passport")
        seria_number.send_keys("12 123456")
        phone = driver.find_element_by_name("phone")
        phone.send_keys("+7(234)123-12-12")
        email1 = driver.find_element_by_name("email1")
        email1.send_keys("knikitin@avinfors.ru")
        email2 = driver.find_element_by_name("email2")
        email2.send_keys("knikitin@avinfors.ru")

    def fill_frame(self):
        self.first_page()
        self.begin_date(6)
        self.insurer_info()


travel=Travel()