from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.allsportgames_page import AllSportGamesElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AllSportGamesActions(Base_Setup.BSetup):

    def Assert_Quick_Transfer_Modal_Dialog(self):
            wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, AllSportGamesElement.quick_transfer_button))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            quick_transfer = self.driver.find_element_by_class_name(AllSportGamesElement.quick_transfer_button).is_displayed()
            self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not shown as expected.")

    def Navigate_to_Sports_Book(self):
            LoginpageActions.Login_to_Mainpage(self)
            MainpageActions.Access_to_AllSportGames_Page(self)
            # Wait the page loads
            wait_page_load = EC.element_to_be_clickable((By.XPATH, AllSportGamesElement.sports_book))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            print("<li>" + "Click on Sports Book" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(AllSportGamesElement.sports_book).click()

