import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class PayOnlinePage(BasePage):
    def fill(self):
        driver = self.driver
        # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "ccnumber")))
        time.sleep(5)
        ccnumber = driver.find_element_by_id("ccnumber")
        ccnumber.click()
        ccnumber.send_keys("4111111111111111")