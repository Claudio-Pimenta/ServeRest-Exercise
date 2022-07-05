from Pages.BasePage import BasePage
from Locators import Locators

class LoginPage(BasePage):    
    
    def login(self, email, password):
        self.do_send_keys(Locators.email_input, email)
        self.do_send_keys(Locators.password_input, password)
        self.do_click(Locators.login_button)
        
    def logout(self):
        self.do_click(Locators.logout_button)