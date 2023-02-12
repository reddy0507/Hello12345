import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
class Test_001_login:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homepage(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = webdriver.Chrome()
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURl)
        #self.driver.implicitly_wait(10)
        time.sleep(10)
        act_title = self.driver.title
        print(act_title)
        if act_title == "OrangeHRM":
            self.logger.info("**** Home page title test passed ****")
            assert True
            self.driver.close()
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURl)
        self.driver.implicitly_wait(10)
        self.loginpage = Login(self.driver)
        self.loginpage.setusername(self.username)
        self.loginpage.setpassword(self.password)
        self.loginpage.login()
        act_title  = self.driver.title
        if act_title == "OrangeHRM":
            self.logger.info("****Login test passed ****")
            time.sleep(10)
            assert True
            self.driver.close()
        else:
            self.logger.error("****Login test failed ****")
            time.sleep(10)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close()


