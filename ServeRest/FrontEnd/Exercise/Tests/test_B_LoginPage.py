from Pages.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import conftest


class TestLogin(conftest):
    
    def test_valid_login_admin(self, driver_init):
        loginPage = LoginPage(driver_init)
        loginPage.login("name1@hotmail.com", "123")
        WebDriverWait(driver_init, 10).until(EC.url_to_be("https://front.serverest.dev/admin/home"))
        loginPage.logout()
        
    def test_valid_login_not_admin(self, driver_init):
        loginPage = LoginPage(driver_init)
        loginPage.login("name2@hotmail.com", "123")
        WebDriverWait(driver_init, 10).until(EC.url_to_be("https://front.serverest.dev/home"))
        loginPage.logout()
    
    def test_invalid_login(self, driver_init):
        loginPage = LoginPage(driver_init)
        loginPage.login("invalidemail@hotmail.com", "123")
        WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, "//span[.='Email e/ou senha inválidos']")))
