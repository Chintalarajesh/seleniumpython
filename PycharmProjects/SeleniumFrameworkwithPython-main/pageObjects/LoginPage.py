from selenium.webdriver.common.by import By
from utilites import baseClass
from utilites import XLUtils
from utilites.customlogger import LogGen


class LoginPage():
    path = ".//TestData/Punters_pages.xlsx"
    logger = LogGen.loggen()
    base = baseClass.BaseCase()
    Popup_xpath = "//button[contains(text(),'Agree')]"
    PuntersPageImage_xpath = "(//a[@href='https://www.thepunterspage.com'])[1]"
    PuntersPageMainTitle_xpath = "//h1[contains(text(),'ThePuntersPage (TPP)')]"
    PuntersPageSubTitle_xpath = "//h2[contains(text(),'BEST FREE BETS ')]"
    BestBookiesTab_xpath = "//li[contains(text(),'Best Bookies')]"
    BestBookiesHighlightTab_xpath = "//li[@class='bookietab-link current'][text()='Best Bookies']"
    BestBonusTab_xpath = "//li[contains(text(),'Best Bonus')]"
    BestBonusHighlightTab_xpath = "//li[@class='bookietab-link current'][text()='Best Bonus']"
    BestAppTab_xpath = "//li[contains(text(),'Best App')]"
    BestAppHighlightTab_xpath = "//li[@class='bookietab-link current'][text()='Best App']"
    BestOddsTab_xpath = "//li[contains(text(),'Best Odds')]"
    BestOddsHighlightTab_xpath = "//li[@class='bookietab-link current'][text()='Best Odds']"
    NewestBookiesTab_xpath = "//li[contains(text(),'Newest Bookies')]"
    NewestBookiesHighlightTab_xpath = "//li[@class='bookietab-link current'][text()='Newest Bookies']"

    # lets create a constructor to initiate our driver, and for that we will create our constructor which will invoke at the time of object creation.
    # what this constructor is doing is capturing the driver from the test case
    def __init__(self, driver):
        self.driver = driver

    def click_popup(self):
        self.driver.find_element(by=By.XPATH, value=self.Popup_xpath).click()

    def verify_punterspageimage(self):
        self.driver.find_element(by=By.XPATH, value=self.punterspageimage_xpath)

    def verify_punterspagemaintitle(self):
        self.driver.find_element(by=By.XPATH, value=self.PuntersPageMainTitle_xpath)

    def BestBookiesTab(self):
        if self.driver.find_element(By.XPATH, self.BestBookiesTab_xpath).is_displayed():
           self.logger.info("best bookies tab is displayed")
           assert True
        else:
            self.logger.info("best bookies tab is not displayed")
            assert False

    def verify_BestBookiesHighlightTab(self):
        # self.driver.find_element(By.XPATH, "//li[@class='bookietab-link current'][text()='Best Bookies']")
        if self.driver.find_element(By.XPATH, self.BestBookiesHighlightTab_xpath).is_displayed():
            self.logger.info("best bookies highlight tab is displayed")
            assert True
        else:
            self.logger.info("best bookies highlight tab is not displayed")
            assert False

    def click_BestBonusTab(self):
        if self.driver.find_element(By.XPATH, self.BestBonusTab_xpath).is_displayed():
            self.logger.info("best bonus tab is displayed")
            BestBonusTab = self.driver.find_element(By.XPATH, self.BestBonusTab_xpath)
            # self.driver.execute_script("arguments[0].click();", BestBonusTab)
            # self.base.click(BestBonusTab)
            self.base.js_click(BestBonusTab)
            assert True
        else:
            self.logger.info("best bonus tab is not displayed")
            assert False

    def verify_BestBonusHighlightTab(self):
        if self.driver.find_element(By.XPATH, self.BestBonusHighlightTab_xpath).is_displayed():
            self.logger.info("best bonus highlight tab is displayed")
            assert True
        else:
            self.logger.info("best bonus highlight tab is not displayed")
            assert False

    def click_BestAppTab(self):
        if self.driver.find_element(By.XPATH, self.BestAppTab_xpath).is_displayed():
            BestApp = self.driver.find_element(By.XPATH, self.BestAppTab_xpath)
            self.driver.execute_script("arguments[0].click();", BestApp)
            self.logger.info("best app tab is displayed")
            assert True
        else:
            self.logger.info("best app tab is not displayed")
            assert False

    def verify_BestAppHighlightTab(self):
        if self.driver.find_element(By.XPATH, self.BestAppHighlightTab_xpath).is_displayed():
            self.logger.info("best app high light tab is displayed")
            assert True
        else:
            self.logger.info("best app high light tab is not displayed")
            assert False

    def click_BestOddsTab(self):
        if self.driver.find_element(By.XPATH, self.BestOddsTab_xpath).is_displayed():
            BestOdds = self.driver.find_element(By.XPATH, self.BestOddsTab_xpath)
            self.driver.execute_script("arguments[0].click();", BestOdds)
            self.logger.info("best odds tab is displayed")
            assert True
        else:
            self.logger.info("best odds tab is not displayed")
            assert False

    def verify_BestOddsHighlightTab(self):
        if self.driver.find_element(By.XPATH, self.BestOddsHighlightTab_xpath).is_displayed():
            self.logger.info("best odds high light tab is displayed")
            assert True
        else:
            self.logger.info("best odds high light tab is not displayed")
            assert False
    def click_NewestBookiesTab(self):
        if self.driver.find_element(By.XPATH, self.NewestBookiesTab_xpath).is_displayed():
            NewestBookies = self.driver.find_element(By.XPATH, self.NewestBookiesTab_xpath)
            self.driver.execute_script("arguments[0].click();", NewestBookies)
            self.logger.info("Newest bookies tab is displayed")
            assert True
        else:
            self.logger.info("best odds tab is not displayed")
            assert False
    def verify_NewestBookiesHighlightTab(self):
        if self.driver.find_element(By.XPATH, self.NewestBookiesHighlightTab_xpath).is_displayed():
            self.logger.info("best Newest bookies high light tab is displayed")
            assert True
        else:
            self.logger.info("best Newest bookies high light tab is not displayed")
            assert False
    def readdata(self):
       self.backgrouddata = XLUtils.readData(self.path, 'BestBookies_LATESTOFFER', 2, 1)
       print(self.backgrouddata)

    # def setUsername(self, username):
    #     self.driver.find_element_by_id(self.textbox_username_id).clear()
    #     self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    #
    # def setPassword(self, password):
    #     self.driver.find_element_by_id(self.textbox_password_id).clear()
    #     self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    #
    # def clickOnLogin(self):
    #     self.driver.find_element_by_xpath(self.button_login_xpath).click()
    #
    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_LinkText).click()




