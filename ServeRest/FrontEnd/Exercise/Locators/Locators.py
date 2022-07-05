from selenium.webdriver.common.by import By

# This File Contains All Necessary Locators

# Login Page

email_input = (By.CSS_SELECTOR, "[data-testid=email]")
password_input = (By.CSS_SELECTOR, "[data-testid=senha]")
login_button = (By.CSS_SELECTOR, "[data-testid=entrar]")
register_button = (By.CSS_SELECTOR, "[data-testid=cadastrar]")

#Signup Page

name_input = (By.CSS_SELECTOR, "[data-testid=nome]")
create_password_input = (By.CSS_SELECTOR, "[data-testid=password]")
admin_checkbox = (By.CSS_SELECTOR, "[data-testid=checkbox]")

#Home Page

logout_button = (By.CSS_SELECTOR, "[data-testid=logout]")