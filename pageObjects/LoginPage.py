from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_name = "username"
    textbox_Password_name = "password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
    
    def setpassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_Password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_Password_name).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()