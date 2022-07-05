from Pages.BasePage import BasePage
from Locators import Locators

class SignupPage(BasePage):    
    
    def create_account(self, name, email, password, isAdmin):
        if (self.driver.current_url != "https://front.serverest.dev/cadastrarusuarios"):
            self.do_click(Locators.register_button)
        self.do_send_keys(Locators.name_input, name)
        self.do_send_keys(Locators.email_input, email)
        self.do_send_keys(Locators.create_password_input, password)
        if (isAdmin):
            self.do_click(Locators.admin_checkbox)
        self.do_click(Locators.register_button)
        
    def logout(self):
        self.do_click(Locators.logout_button)
        