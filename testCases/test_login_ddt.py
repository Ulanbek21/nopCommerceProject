#---------------------------------------------DATA DRIVEN TEST---------------------------------------------------------
# (Python, Selenium, PyTest, Page Object Model, HTML Reports)

# 1) Creat Test Data EXCEL FILE
# 2) we need to creat XLUtils.xlsx-------> utiliti file
import sys
sys.path.append('.')
import pytest 
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
from utilites  import XLUtils 
import time
from utilites.XLUtils import openpyxl

# Start writing actual test

# class Test_002_DDT_Login:
#     baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'              #'admin'
#     logger = LogGen.Loggen()
#     path = './/TestData//LoginData.xlsx'

# # Write Login test
#     def test_Login_ddt(self,setup):
#         self.logger.info('********** Started Test_002_DDT_Login **********')
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp = LoginPage(self.driver)

#         self.rows = XLUtils.getRowCount(self.path,'Sheet1')
#         lst_status = []

#         for r in range(2,self.rows + 1):
#             self.user = XLUtils.readDatA(self.path,'Sheet1',r,1)# it will retreave username
#             self.password = XLUtils.readDatA(self.path,'Sheet1',r,2)# it will retreave password
#             self.exp = XLUtils.readDatA(self.path,'Sheet1',r,3) #it will retreave expected value

#             self.lp.setUserName(self.user)
#             self.lp.setPassword(self.password)
#             self.lp.clickLogin()
#             time.sleep(3)
#             act_title = self.driver.title
#             exp_title = 'Dashboard / nopCommerce administration'
#             # self.driver.close()

#             if act_title == exp_title: # login success
#                 if self.exp == 'pass':
#                     self.logger.info('****** Passed ******')
#                     self.lp.clicklogout()
#                     lst_status.append('Pass')
#                 elif self.exp == 'fail':
#                     self.logger.info('***** Failed *****')
#                     lst_status.append('Pass')
#                     self.lp.clicklogout()
#             elif act_title != exp_title: # login is not soccesful
#                 if self.exp == 'pass':
#                     self.logger.info('****** Failed ******')  
#                     lst_status.append('Pass')  
#                 elif self.exp == 'fail':
#                     self.logger.info('***** Paased *****')
#                     lst_status.append('Pass')

#         if 'Fail' not in lst_status:
#             self.logger.error('****** DDT Login test failed ******')
#             assert False

#         else:
#             self.logger.error('****** DDT Login test passed ******')
#             assert True
#         self.logger('********** Finished Test_002_DDT_Login **********')
#         self.driver.close()


#------------------------------------------------------------------------------------------------------------------------------

class Test_002_DDT_Login:
    baseURL= ReadConfig.getApplicationURL()             #'https://admin-demo.nopcommerce.com/login'              #'admin'
    logger = LogGen.Loggen()
    path = './/TestData//LoginData.xlsx'
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clicklogout()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info(" **** passed **** ")
                    lst_status.append(" Pass ")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 *************")



        







                


            