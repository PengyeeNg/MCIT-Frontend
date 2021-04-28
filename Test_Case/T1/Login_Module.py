import unittest
from selenium.webdriver import ActionChains
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Elements.T1.main_page import MainpageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginModule(Base_Setup.BSetup):

    def TC_Login_01_Valid_Login(self):
        print("<b> Expected Results: Login to Main Page with valid username and password. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)

    def test_TC_Login_02_Logout(self):
        print("<b> Expected Results: Login from the account. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        self.driver.implicitly_wait(10)
        scroll_down = self.driver.find_element_by_xpath(MainpageElement.logout_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_down).perform()
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on Log Out button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.logout_button).click()
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.sign_up_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        logout_from_main = self.driver.find_element_by_class_name(MainpageElement.sign_up_button).is_displayed()
        self.assertTrue(logout_from_main, "User is not able to logout from the account.")


if __name__ == '__main__':
    unittest.main()
