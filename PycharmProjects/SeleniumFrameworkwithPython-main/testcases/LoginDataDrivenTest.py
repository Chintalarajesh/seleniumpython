import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilites import XLUtils
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen



class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData/Punters_pages.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("**************************Test_002_login_ddt test**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'BestBookies_LATESTOFFER')
        print("number of rows in Excel:", self.rows)
        # empty list variable
        list_status=[]
        MrMegaBetGetRibbon = self.driver.find_element(By.XPATH, self.MrMegaBetGEetRibbon_Xpath)
        MrMegaBetGetRibbon.clear()

        self.backgroundcolor = XLUtils.readData(self.path, 'BestBookies_LATESTOFFER', 2, 1)
        self.logger.info(self.backgroundcolor)
        # self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
        # self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

