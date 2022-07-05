from Pages.SignupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import conftest


class TestSignup(conftest):
  
    
    def test_create_valid_admin_account(self, driver_init):
        signupPage = SignupPage(driver_init)
        signupPage.create_account("Name1", "name1@hotmail.com", "123", True)
        WebDriverWait(driver_init, 10).until(EC.url_to_be("https://front.serverest.dev/admin/home"))
        signupPage.logout()
       
    def test_create_valid_not_admin_account(self, driver_init):
        signupPage = SignupPage(driver_init)
        signupPage.create_account("Name2", "name2@hotmail.com", "123", False)
        WebDriverWait(driver_init, 10).until(EC.url_to_be("https://front.serverest.dev/home"))
        signupPage.logout()
        
    def test_create_invalid_repeated_email(self, driver_init):
        signupPage = SignupPage(driver_init)
        signupPage.create_account("Name1Repeated", "name1@hotmail.com", "123", False)
        WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, "//span[.='Este email já está sendo usado']")))
        
    def test_create_invalid_empy_email(self, driver_init):
        signupPage = SignupPage(driver_init)
        signupPage.create_account("NameInvalid", "", "123", False)
        WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, "//span[.='Email é obrigatório']")))      
     
    #Bug Cria utilizador sem a nome
        
    #def test_create_invalid_empty_name(self, driver_init):
    #    signupPage = SignupPage(driver_init)
    #    signupPage.create_account("", "email@email.com", "123", False)
    #    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, "//span[.='Nome é obrigatório']")))
    
    #Bug Cria utilizador sem a pass
    
    #def test_create_invalid_empty_password(self, driver_init):
    #    signupPage = SignupPage(driver_init)
    #    signupPage.create_account("Nome", "email@email.com", "", False)
    #    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, "//span[.='Nome é obrigatório']")))
        