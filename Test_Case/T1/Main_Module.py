import unittest
from Setup.T1 import Base_Setup
from Actions.T1.main_page import MainpageActions
from Actions.T1.login_page import LoginpageActions
from Elements.T1.main_page import MainpageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainModule(Base_Setup.BSetup):

    def TC_Main_01_Navigate_to_Main_Page(self):
        print("<b> Expected Results: Able to access to main page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)

    def TC_Main_02_Navigate_to_Login_Page(self):
        print("<b> Expected Results: Navigated to login page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Login_Page(self)

    def TC_Main_03_Navigate_to_SignUp_Page(self):
        print("<b> Expected Results: Navigated to sign up page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_SignUp_Page(self)

    def TC_Main_04_Navigate_to_All_Slot_Games_Page(self):
        print("<b> Expected Results: Navigated to All Slot Games page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_AllSlotGames_Page(self)

    def TC_Main_05_Navigate_to_All_Live_Games_Page(self):
        print("<b> Expected Results: Navigated to All Live Games page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_AllLiveGames_Page(self)

    def TC_Main_06_Navigate_to_All_Sport_Games_Page(self):
        print("<b> Expected Results: Navigated to All Sport Games page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_AllSportGames_Page(self)

    def TC_Main_07_Navigate_to_Promotion_Page(self):
        print("<b> Expected Results: Navigated to Promotion page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Promotion_Page(self)

    def TC_Main_08_Navigate_to_Providers_Page(self):
        print("<b> Expected Results: Navigated to Providers page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Providers_Page(self)

    def TC_Main_09_View_Notification(self):
        print("<b> Expected Results: Navigated to Notification Page by clicking on notification icon. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        self.driver.find_element_by_class_name(MainpageElement.notification_icon).click()
        # Wait poge loads
        wait_login_page = EC.text_to_be_present_in_element((By.CLASS_NAME, MainpageElement.notification_page_title), "Notifications")
        WebDriverWait(self.driver, 20).until(wait_login_page)
        notification_title = self.driver.find_element_by_class_name(MainpageElement.notification_page_title).text
        self.assertEqual(notification_title, "Notifications", "User is not able to navigate to Notification page by clicking on Notification icon.")

    def test_TC_Main_10_View_Deposit(self):
        print("<b> Expected Results: Navigated to Deposit Page by clicking on Deposit button. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Deposit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.deposit_button_at_main).click()
        # Wait poge loads
        wait_login_page = EC.text_to_be_present_in_element((By.CSS_SELECTOR, MainpageElement.deposit_page_title), "Deposit")
        WebDriverWait(self.driver, 20).until(wait_login_page)
        deposit_button = self.driver.find_element_by_css_selector(MainpageElement.deposit_page_title).text
        self.assertEqual(deposit_button, "Deposit", "User is not able to navigate to Deposit page by clicking on Deposit button.")


if __name__ == '__main__':
    unittest.main()

