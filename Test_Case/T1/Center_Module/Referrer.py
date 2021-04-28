import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.center_page import ReferrerElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CenterReferrerModule(Base_Setup.BSetup):

    def test_TC_Center_Referrer_01_View_Membership_Information(self):
        print("<b> Expected Results: Able to view membership information. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Referrer(self)
        wait_page_load = EC.presence_of_element_located((By.XPATH, ReferrerElement.memberlist_tab))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        show_memberlisttab = self.driver.find_element_by_xpath(ReferrerElement.memberlist_tab).is_displayed()
        self.assertTrue(show_memberlisttab, "Not able to access to Referrer Page.")
        print("<li>" + "Click on Member List" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ReferrerElement.memberlist_tab).click()
        print("<li>" + "Click on User ID" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ReferrerElement.user_id_link).click()
        # Wait
        wait_membership_info = EC.element_to_be_clickable((By.CLASS_NAME, ReferrerElement.user_id_exit))
        WebDriverWait(self.driver, 20).until(wait_membership_info)
        # Assert
        show_memberinfo = self.driver.find_element_by_class_name(ReferrerElement.user_id_exit).is_displayed()
        self.assertTrue(show_memberinfo, "Not able to access to Membership Information.")

    def test_TC_Center_Referrer_02_View_Report(self):
        print("<b> Expected Results: Able to view report. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Referrer(self)
        wait_page_load = EC.presence_of_element_located((By.XPATH, ReferrerElement.memberlist_tab))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        show_memberlisttab = self.driver.find_element_by_xpath(ReferrerElement.memberlist_tab).is_displayed()
        self.assertTrue(show_memberlisttab, "Not able to access to Referrer Page.")
        print("<li>" + "Click on Report" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ReferrerElement.report_tab).click()
        wait_deposit_report = EC.presence_of_element_located((By.CLASS_NAME, ReferrerElement.report_deposit))
        WebDriverWait(self.driver, 20).until(wait_deposit_report)
        # Assert
        show_deposit_report = self.driver.find_element_by_class_name(ReferrerElement.report_deposit).is_displayed()
        self.assertTrue(show_deposit_report, "Not able to access to Report.")

    def test_TC_Center_Referrer_03_View_Bet_Record(self):
        print("<b> Expected Results: Able to Bet Record. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Referrer(self)
        wait_page_load = EC.presence_of_element_located((By.XPATH, ReferrerElement.memberlist_tab))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        show_memberlisttab = self.driver.find_element_by_xpath(ReferrerElement.memberlist_tab).is_displayed()
        self.assertTrue(show_memberlisttab, "Not able to access to Referrer Page.")
        print("<li>" + "Click on Bet Record" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ReferrerElement.bet_record_tab).click()
        wait_bet_record = EC.presence_of_element_located((By.CLASS_NAME, ReferrerElement.bet_record_filter))
        WebDriverWait(self.driver, 20).until(wait_bet_record)
        # Assert
        show_bet_record = self.driver.find_element_by_class_name(ReferrerElement.bet_record_filter).is_displayed()
        self.assertTrue(show_bet_record, "Not able to access to Bet Record.")




if __name__ == '__main__':
    unittest.main()
