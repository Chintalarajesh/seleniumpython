import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen


class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl()
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getUserPassword()
    # path = ".//TestData/Punters_pages.xlsx"
    logger = LogGen.loggen()



    @pytest.mark.filterwarnings
    @pytest.mark.sanity
    # @pytest.fixture()
    def test_login(self, setup):

        self.logger.info("**********************************Testing homepage title***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
    #     yield
    #     self.driver.quit()
    # def test_ClickTabs(self):
        act_title = self.driver.title
        self.logger.info(act_title)
        if act_title == "Best UK Online Betting (2023) | Guides, Free Bets, Odds, Offers & Stats":
            assert True
            # self.driver.close()
        else:
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            # self.driver.close()
            assert False

        self.lp = LoginPage(self.driver)
        self.lp.click_popup()
        self.driver.execute_script("document.body.style.zoom='70%'")
        time.sleep(5)
        self.lp.BestBookiesTab()
        self.lp.verify_BestBookiesHighlightTab()
        self.lp.click_BestBonusTab()
        self.lp.verify_BestBonusHighlightTab()
        self.lp.click_BestAppTab()
        self.lp.verify_BestAppHighlightTab()
        self.lp.click_BestOddsTab()
        self.lp.verify_BestOddsHighlightTab()
        self.lp.click_NewestBookiesTab()
        self.lp.verify_NewestBookiesHighlightTab()
        self.lp.readdata()
        # self.driver.quit()





        # act_firstTab = self.lp.BestBookiesTab().get_attribute("innerHTML")
        # try:
        #   self.lp.BestBookiesTab().is_displayed()
        #   self.logger.info("print bestbookies")
        #   assert True
        # except AttributeError:
        #     self.driver.save_screenshot(".\\Screenshots\\punters\\" + "test_homepageTitle.png")
        # if self.lp.BestBookiesTab().is_displayed():
        #      self.logger.info("print bestbookies")
        #      assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\punters\\" + "test_homepageTitle.png")
        #     assert False
        #
        # if self.lp.BestBookiesHighlightTab().is_displayed():
        #     self.logger.info("bestbookies highlight tab is displayed")
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
        #     assert False



