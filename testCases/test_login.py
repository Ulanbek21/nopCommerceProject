import sys
sys.path.append('.')
import pytest
# from selenium import webdriver
# import pytest
            # import class form POM then modul[filename] pakge import file where you creat class
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

#---------------------------------------------
            # import class form POM then modul[filename] pakge import file where you creat class
            #from pageObjects.LoginPage import LoginPage

# Start writing actual test

# class Test_001_Login:
#     baseURL = 'https://admin-demo.nopcommerce.com/login'
#     username = 'admin@yourstore.com'
#     password = 'admin'
#     # driver = webdriver.Chrome()

# # Validation point TC 
#     def test_homePageTitle(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         # time.sleep(2)
#         self.driver.close()
#         if act_title == 'Your store. Login':
#             assert True
#         else:
#             assert False

# # Write Login test
#     def test_Login(self,setup):
#         self.driver = setup
#         self.lp = LoginPage(self.driver)
#         self.driver.get(self.baseURL)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         # time.sleep(2)
#         self.driver.close()
#         if act_title == 'Dashboard / nopCommerce administration':
#             assert True
#         else:
#             assert False
#---------------------------------------------Screen Shot------------------------------------------------------------

# class Test_001_Login:
#     baseURL = 'https://admin-demo.nopcommerce.com/login'
#     username = 'admin@yourstore.com'
#     password = 'admin'
#     # driver = webdriver.Chrome()

# # Validation point TC 
#     def test_homePageTitle(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         if act_title == 'Your store. Login':
#             # self.driver.close()
#             assert True
#         else:
#             self.driver.save_screenshot('.//Screenshots//' + 'test_homePageTitle.png')# use .// making rel path
#             self.driver.close()
#             assert False

# # Write Login test
#     def test_Login(self,setup):
#         self.driver = setup
#         self.lp = LoginPage(self.driver)
#         self.driver.get(self.baseURL)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         # self.driver.close()
#         if act_title == 'Dashboard / nopCommerce administration':
#             self.driver.close()
#             assert True
#         else:
#             self.driver.save_screenshot('.//Screenshots//' + 'test_homePageTitle.png')# use .// making rel path
#             self.driver.close()
#             assert False

#---------------------------------------------uing data from UTILITIS pack------------------------------------------------------------
                                #from utilites.readProperties import ReadConfig
# class Test_001_Login:
#     baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'
#     username = ReadConfig.getUseremail()               #'admin@yourstore.com'
#     password =  ReadConfig.getPassword()               #'admin'

# # Validation point TC 
#     def test_homePageTitle(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Your store. Login':
#             assert True
#         else:
#             assert False

# # Write Login test
#     def test_Login(self,setup):
#         self.driver = setup
#         self.lp = LoginPage(self.driver)
#         self.driver.get(self.baseURL)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Dashboard / nopCommerce administration':
#             assert True
#         else:
#             assert False
#---------------------------------------------Generating Loggs costum logs----------------------------------    
    #from utilites.customLogger import LogGen

# class Test_001_Login:
#     baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'
#     username = ReadConfig.getUseremail()               #'admin@yourstore.com'
#     password =  ReadConfig.getPassword()               #'admin'
#     logger = LogGen.Loggen()
# # Validation point TC 
#     def test_homePageTitle(self,setup):
#         self.logger.info('********** Test_001_Login **********')

#         self.logger.info('********** Starter Home Page title test **********')
#         self.driver = setup

#         self.logger.info('********** Opening URL my app **********')

#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Your store. Login111':
#             self.logger.info('********** home page title test passed **********')
#             assert True
#         else:
#             self.logger.error('********** home page title test failed **********')
#             assert False

# # Write Login test
#     def test_Login(self,setup):
#         self.logger.info('********** Started login test **********')
        
#         self.driver = setup
#         self.lp = LoginPage(self.driver)
#         self.driver.get(self.baseURL)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Dashboard / nopCommerce administration':
#             self.logger.info('********** Login test passed **********')
#             assert True
#         else:
#             self.logger.error('********** Login test failed **********')
#             assert False
#---------------------------------------------Paralel test
# class Test_001_Login:
#     baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'
#     username = ReadConfig.getUseremail()               #'admin@yourstore.com'
#     password =  ReadConfig.getPassword()               #'admin'
#     logger = LogGen.Loggen()
# # Validation point TC 
#     def test_homePageTitle(self,setup):
#         self.logger.info('********** Test_001_Login **********')

#         self.logger.info('********** Starter Home Page title test **********')
#         self.driver = setup

#         self.logger.info('********** Opening URL my app **********')

#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Your store. Login':
#             self.logger.info('********** home page title test passed **********')
#             assert True
#         else:
#             self.logger.error('********** home page title test failed **********')
#             assert False

# # Write Login test
#     def test_Login(self,setup):
#         self.logger.info('********** Started login test **********')
        
#         self.driver = setup
#         self.lp = LoginPage(self.driver)
#         self.driver.get(self.baseURL)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == 'Dashboard / nopCommerce administration':
#             self.logger.info('********** Login test passed **********')
#             assert True
#         else:
#             self.logger.error('********** Login test failed **********')
#             assert False

#---------------------------------------------DATA DRIVEN TEST---------------------------------------------------------
# (Python, Selenium, PyTest, Page Object Model, HTML Reports)

# 1) Creat Test Data EXCEL FILE
# 2) we need to creat XLUtils.xlsx-------> utiliti file



class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'
    username = ReadConfig.getUseremail()               #'admin@yourstore.com'
    password =  ReadConfig.getPassword()               #'admin'
    logger = LogGen.Loggen()
# Validation point TC 
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('********** Test_001_Login **********')

        self.logger.info('********** Starter Home Page title test **********')
        self.driver = setup

        self.logger.info('********** Opening URL my app **********')

        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Your store. Login':
            self.logger.info('********** home page title test passed **********')
            assert True
        else:
            self.logger.error('********** home page title test failed **********')
            assert False

# Write Login test
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info('********** Started login test **********')
        
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info('********** Login test passed **********')
            assert True
        else:
            self.logger.error('********** Login test failed **********')
            assert False