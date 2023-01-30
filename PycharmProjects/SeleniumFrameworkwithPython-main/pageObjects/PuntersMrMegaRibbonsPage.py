import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilites.customlogger import LogGen


class PuntersMrMegaRibbonsPage:

    logger = LogGen.loggen()

    MrMegaBetGEetRibbon_Xpath = "(//span[text()='Bet £15 Get £10'])[2]"
    MrMegaHomePage_Xpath = "//div[@class='play-now']"
    MrMegaClaimBonusRibbon_Xpath = "(//span[text()='CLAIM BONUS'])[2]"
    MrMegaDetailsButton_Xpath = "(//div[text()='DETAILS'])[2]"
    MrMegaExpandingDetailsButton_Xpath = "//button[@class='bookietabs-collapsible active']"
    MrMegaExpandingDetails_Xpath = "(//li[text()=' Cash Out'])[2]"
    MrMegaTCApply_Xpath = "(//div[text()='T&Cs APPLY, 18+ ONLY'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickBet15Get10InMrMega_VerifyRespectiveWindowIsDisplaying(self):
        MrMegaBetGetRibbon = self.driver.find_element(By.XPATH, self.MrMegaBetGEetRibbon_Xpath)
        if MrMegaBetGetRibbon.is_displayed():
          # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_BeforeClickMrMegaBetGetRibbon.png")
          self.logger.info("MrMega bet get ribbon is displayed")
          self.driver.execute_script("arguments[0].click();", MrMegaBetGetRibbon)
          # window handle
          handles = self.driver.window_handles
          size = len(handles)
          parent_handle = self.driver.current_window_handle
          for x in range(size):
             self.driver.switch_to.window(handles[x])
          WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, self.MrMegaHomePage_Xpath)))
          ext_NextWindowTitle = "mr. Mega"
          MrMegaHomePage = self.driver.find_element(By.XPATH, self.MrMegaHomePage_Xpath)
          if MrMegaHomePage.is_displayed():
              # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_AfterClickMrMegaBetGetRibbon.png")
              self.logger.info("MrMega home page is displayed")
              act_NextWindowTitle = self.driver.title
              assert act_NextWindowTitle == ext_NextWindowTitle
              assert True
          else:
              self.logger.info("MrMega home page is not displayed")
              assert False
        else:
            self.logger.info("MrMega bet get ribbon is not displayed")
            assert False
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_AfterCloseMrMegaHomePage.png")
        time.sleep(3)
    def clickClaimBonusInMrMega_VerifyRespectiveWindowIsDisplaying(self):
        MrMegaClaimBonusRibbon = self.driver.find_element(By.XPATH, self.MrMegaClaimBonusRibbon_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", MrMegaClaimBonusRibbon)
        if MrMegaClaimBonusRibbon.is_displayed():
            # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_BeforeClickMrMegaClaimBonus.png")
            self.logger.info("MrMega claim bonus ribbon is displayed")
            self.driver.execute_script("arguments[0].click();", MrMegaClaimBonusRibbon)
            # window handle
            handles = self.driver.window_handles
            size = len(handles)
            parent_handle = self.driver.current_window_handle
            for x in range(size):
                self.driver.switch_to.window(handles[x])
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, self.MrMegaHomePage_Xpath)))
            ext_NextWindowTitle = "mr. Mega"
            MrMegaHomePage = self.driver.find_element(By.XPATH, self.MrMegaHomePage_Xpath)
            if MrMegaHomePage.is_displayed():
                # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_AfterClickMrMegaClaimBonus.png")
                self.logger.info("MrMega home page is displayed")
                act_NextWindowTitle = self.driver.title
                assert act_NextWindowTitle == ext_NextWindowTitle
                assert True
            else:
                self.logger.info("MrMega home page is not displayed")
                assert False
        else:
            self.logger.info("MrMega claim bonus ribbon is not displayed")
            assert False
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_AfterCloseMrMegaHomePage.png")
        time.sleep(3)
    def clickDetailsButtonInMrMega_VerifyTheSectionsIsExpanding(self):
        MrMegaDetailsButton = self.driver.find_element(By.XPATH, self.MrMegaDetailsButton_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", MrMegaDetailsButton)
        # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_BeforeClickMrMegaDetailButton.png")
        self.driver.execute_script("arguments[0].click();", MrMegaDetailsButton)
        MrMegaExpandingDetailsButton = self.driver.find_element(By.XPATH, self.MrMegaExpandingDetailsButton_Xpath)
        MrMegaTCApply = self.driver.find_element(By.XPATH, self.MrMegaTCApply_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", MrMegaTCApply)
        # self.driver.save_screenshot(".\\Screenshots\\PuntersMrMegaRibbons\\" + "test_AfterClikMrMegaDetailButton.png")
        self.driver.execute_script("arguments[0].scrollIntoView();", MrMegaExpandingDetailsButton)
        if MrMegaExpandingDetailsButton.is_displayed():
            self.logger.info("MrMega expanding details button is displayed")
            MrMegaExpandingDetails = self.driver.find_element(By.XPATH, self.MrMegaExpandingDetails_Xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", MrMegaExpandingDetails)
            assert True
            if MrMegaExpandingDetails.is_displayed():
                self.logger.info("MrMega expanding details is displayed")
                assert True
        else:
            self.logger.info("MrMega expanding details button is displayed")
            assert False