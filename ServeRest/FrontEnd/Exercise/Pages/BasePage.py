from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# This Page contains custom functions accessible for all tests

class BasePage:
    
    @pytest.mark.usefixtures("driver_init")
    def __init__(self, driver):
        self.driver = driver
    
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear() 
    #   time.sleep(1)  Use to see SignUp tests bugs 
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
