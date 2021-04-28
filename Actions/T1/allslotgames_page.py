import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.allslotgames_page import AllSlotGamesElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Elements.T1.main_page import MainpageElement

class AllSlotGamesActions(Base_Setup.BSetup):

    def Assert_Quick_Transfer_Modal_Dialog(self):
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, AllSlotGamesElement.quick_transfer_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        quick_transfer = self.driver.find_element_by_class_name(AllSlotGamesElement.quick_transfer_button).is_displayed()
        self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not shown as expected.")

    def Navigate_back_to_LoginPage(self):
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.sign_up_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        logout_from_main = self.driver.find_element_by_class_name(MainpageElement.sign_up_button).is_displayed()
        self.assertTrue(logout_from_main, "User is not navigated to Login Page.")

    def Navigate_to_RespinMania(self):
        MainpageActions.Access_to_AllSlotGames_Page(self)
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, AllSlotGamesElement.respinmania))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on RespinMania" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(AllSlotGamesElement.respinmania).click()

    def Navigate_to_JinFuXingYun(self):
        MainpageActions.Access_to_AllSlotGames_Page(self)
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, AllSlotGamesElement.jinfuxingyun))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on JinFuXingYun" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(AllSlotGamesElement.jinfuxingyun).click()


if __name__ == '__main__':
    unittest.main()
