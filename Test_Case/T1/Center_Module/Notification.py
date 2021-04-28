import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.center_page import NotificationElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CenterNotificationModule(Base_Setup.BSetup):

    def test_TC_Center_Notification_01_View_Membership_Information(self):
        print("<b> Expected Results: Able to view notification details. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Notification(self)
        wait_page_load = EC.presence_of_element_located((By.XPATH, NotificationElement.notification))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        notification_show = self.driver.find_element_by_xpath(NotificationElement.notification).is_displayed()
        self.assertTrue(notification_show, "Notification is not shown in Notification Page")
        print("<li>" + "Click on Notification in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(NotificationElement.notification).click()
        wait_noti_details = EC.presence_of_element_located((By.CLASS_NAME, NotificationElement.notification_detail))
        WebDriverWait(self.driver, 20).until(wait_noti_details)
        notification_details_show = self.driver.find_element_by_class_name(NotificationElement.notification_detail).is_displayed()
        self.assertTrue(notification_details_show, "User is not able to view the notification details.")



if __name__ == '__main__':
    unittest.main()
