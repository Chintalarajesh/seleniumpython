import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilites.customlogger import LogGen

class PuntersBetTargetRibbonsPage:
    logger = LogGen.loggen()

    BetTargetBetGEetRibbon_Xpath = "(//span[text()='Bet £15 Get £10'])[1]"
    BetTargetHomePage_Xpath = "//a[@id='link-1zb8c43cp59']"
    BetTargetClaimBonusRibbon_Xpath = "(//span[text()='CLAIM BONUS'])[1]"
    BetTargetDetailsButton_Xpath = "(//div[text()='DETAILS'])[1]"
    BetTargetExpandingDetailsButton_Xpath = "//button[@class='bookietabs-collapsible active']"
    BetTargetExpandingDetails_Xpath = "(//li[text()=' Cash Out'])[1]"
    BetTargetTCAppliy_Xpath = "(//div[text()='T&Cs APPLY, 18+ ONLY'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickBet15Get10InBetTarget_VerifyRespectiveWindowIsDisplaying(self):
        BetTargetBetGetRibbon = self.driver.find_element(By.XPATH, self.BetTargetBetGEetRibbon_Xpath)
        if BetTargetBetGetRibbon.is_displayed():
          self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_BeforeClickBetTargetBetGetRibbon.png")
          self.logger.info("Bet target bet get ribbon is displayed")
          self.driver.execute_script("arguments[0].click();", BetTargetBetGetRibbon)
          # window handle
          handles = self.driver.window_handles
          size = len(handles)
          parent_handle = self.driver.current_window_handle
          for x in range(size):
             self.driver.switch_to.window(handles[x])
          WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, self.BetTargetHomePage_Xpath)))
          ext_NextWindowTitle = "BetTarget - Sport welcome offer"
          BetTargetHomePage = self.driver.find_element(By.XPATH, self.BetTargetHomePage_Xpath)
          if BetTargetHomePage.is_displayed():
              self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_AfterClickBetTargetBetGetRibbon.png")
              self.logger.info("Bet target home page is displayed")
              act_NextWindowTitle = self.driver.title
              assert act_NextWindowTitle == ext_NextWindowTitle
              assert True
          else:
              self.logger.info("Bet target home page is not displayed")
              assert False
        else:
            self.logger.info("Bet target bet get ribbon is not displayed")
            assert False
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_AfterCloseBetTargetHomePage.png")
        time.sleep(3)
    def clickClaimBonusInBetTarget_VerifyRespectiveWindowIsDisplaying(self):
        BetTargetClaimBonusRibbon = self.driver.find_element(By.XPATH, self.BetTargetClaimBonusRibbon_Xpath)
        if BetTargetClaimBonusRibbon.is_displayed():
            self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_BeforeClickBetTargetClaimBonus.png")
            self.logger.info("Bet target claim bonus ribbon is displayed")
            self.driver.execute_script("arguments[0].click();", BetTargetClaimBonusRibbon)
            # window handle
            handles = self.driver.window_handles
            size = len(handles)
            parent_handle = self.driver.current_window_handle
            for x in range(size):
                self.driver.switch_to.window(handles[x])
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, self.BetTargetHomePage_Xpath)))
            ext_NextWindowTitle = "BetTarget - Sport welcome offer"
            BetTargetHomePage = self.driver.find_element(By.XPATH, self.BetTargetHomePage_Xpath)
            if BetTargetHomePage.is_displayed():
                self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_AfterClickBetTargetClaimBonus.png")
                self.logger.info("Bet target home page is displayed")
                act_NextWindowTitle = self.driver.title
                assert act_NextWindowTitle == ext_NextWindowTitle
                assert True
            else:
                self.logger.info("Bet target home page is not displayed")
                assert False
        else:
            self.logger.info("Bet target claim bonus ribbon is not displayed")
            assert False
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_AfterCloseBetTargetHomePage.png")
        time.sleep(3)
    def clickDetailsButtonInBetTarget_VerifyTheSectionsIsExpanding(self):
        BetTargetDetailsButton = self.driver.find_element(By.XPATH, self.BetTargetDetailsButton_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", BetTargetDetailsButton)
        self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_BeforeClickBetTargetDetailButton.png")
        self.driver.execute_script("arguments[0].click();", BetTargetDetailsButton)
        BetTargetExpandingDetailsButton = self.driver.find_element(By.XPATH, self.BetTargetExpandingDetailsButton_Xpath)
        BetTargetTCAppliy = self.driver.find_element(By.XPATH, self.BetTargetTCAppliy_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", BetTargetTCAppliy)
        self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_AfterClikBetTargetDetailButton.png")
        self.driver.execute_script("arguments[0].scrollIntoView();", BetTargetExpandingDetailsButton)
        if BetTargetExpandingDetailsButton.is_displayed():
            self.logger.info("Bet target expanding details button is displayed")
            BetTargetExpandingDetails = self.driver.find_element(By.XPATH, self.BetTargetExpandingDetails_Xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", BetTargetExpandingDetails)
            assert True
            if BetTargetExpandingDetails.is_displayed():
                self.logger.info("Bet target expanding details is displayed")
                assert True
        else:
            self.logger.info("Bet target expanding details button is displayed")
            assert False


