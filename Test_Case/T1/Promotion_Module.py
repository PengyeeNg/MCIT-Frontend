import unittest
from Setup.T1 import Base_Setup
from Actions.T1.main_page import MainpageActions
from Actions.T1.login_page import LoginpageActions
from Elements.T1.promotion_page import PromotionElement


class PromotionModule(Base_Setup.BSetup):

    def test_TC_Promotion_01_Access_to_Promotion_Details(self):
        print("<b> Expected Results: Access to Promotion Details. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Promotion_Page(self)
        print("<li>" + "Click on Promotion image to view the details" +  "</li>" + "<br>")
        self.driver.find_element_by_xpath(PromotionElement.promotion_details).click()




if __name__ == '__main__':
    unittest.main()
