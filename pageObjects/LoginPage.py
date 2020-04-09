

# # ----------------------------------Creatin Page Object Class-------------------------for Login Page

# # 1) Creat Class

# # 2) Locaters

# # 3) Constractor

# # 4) Actions

# # ------------------------------------------------------------------
from selenium import webdriver

# # 1) Creat Class
class LoginPage:

# 2) Locaters
    textbox_username_id = 'Email'
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = 'Logout'

# 3) Constractor
    def __init__(self,driver): # Creating constructor for initialazing wit driver
        self.driver = driver

# 4) Actions
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,pwd):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    
    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

#  # ------------------------------------------------------------------

# # Go and creat actual TEsT CASE


