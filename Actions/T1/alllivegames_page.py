import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.alllivegames_page import AllLiveGamesElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AllLiveGamesActions(Base_Setup.BSetup):

    def Navigate_to_3CardBragLive(self):
            LoginpageActions.Login_to_Mainpage(self)
            MainpageActions.Access_to_AllLiveGames_Page(self)
            # Wait the page loads
            wait_page_load = EC.element_to_be_clickable((By.XPATH, AllLiveGamesElement.threecardbraglive))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            print("<li>" + "Click on 3 Card Brag Live" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(AllLiveGamesElement.threecardbraglive).click()

    def Assert_Quick_Transfer_Modal_Dialog(self):
            wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, AllLiveGamesElement.quick_transfer_button))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            quick_transfer = self.driver.find_element_by_class_name(AllLiveGamesElement.quick_transfer_button).is_displayed()
            self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not shown as expected.")