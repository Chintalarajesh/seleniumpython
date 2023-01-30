import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.PuntersBetTargetRibbonsPage import PuntersBetTargetRibbonsPage
from utilites.customlogger import LogGen
from utilites.readProperities import ReadConfig


class Test_PuntersBetTargetRibbons:
    baseUrl = ReadConfig.getApplicationUrl()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_PuntersBetTargetRibbons(self, setup):
        self.logger.info("**********************************Testing homepage title***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        act_title = self.driver.title
        self.logger.info(act_title)
        if act_title == "Best UK Online Betting (2023) | Guides, Free Bets, Odds, Offers & Stats":
            assert True
            # self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\PuntersBetTargetRibbons\\" + "test_homepageTitle.png")
            # self.driver.close()
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.click_popup()
        self.driver.execute_script("document.body.style.zoom='70%'")
        self.pb = PuntersBetTargetRibbonsPage(self.driver)
        self.pb.clickBet15Get10InBetTarget_VerifyRespectiveWindowIsDisplaying()
        self.pb.clickClaimBonusInBetTarget_VerifyRespectiveWindowIsDisplaying()
        self.pb.clickDetailsButtonInBetTarget_VerifyTheSectionsIsExpanding()
        self.driver.quit()