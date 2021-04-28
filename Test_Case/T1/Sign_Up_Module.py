import unittest
from Setup.T1 import Base_Setup
from Elements.T1.signup_page import SignUppageElement
from Elements.T1.login_page import LogInElement
from Elements.T1.main_page import MainpageElement
from Actions.T1.main_page import MainpageActions
from Input_Data.T1.signup_page import SignUpData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class SignUpModule(Base_Setup.BSetup):

    def test_TC_SignUp_01_Sign_Up_New_User(self):
        print("<b> Expected Results: Able to login with registered username and password. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_SignUp_Page(self)
        print("<li>" + "Insert Username: " + SignUpData.new_username + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.username_field).send_keys(SignUpData.new_username)
        print("<li>" + "Insert Mobile Phone: " + SignUpData.phone_number + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.mobile_phone_field).send_keys(SignUpData.phone_number)
        print("<li>" + "Insert Email: " + SignUpData.email + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.email_field).send_keys(SignUpData.email)
        print("<li>" + "Insert Password: " + SignUpData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.password_field).send_keys(SignUpData.password)
        print("<li>" + "Insert Confirm Password: " + SignUpData.confirm_password + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.confirm_password_field).send_keys(SignUpData.confirm_password)
        print("<li>" + "Insert Invitation Code: " + SignUpData.invitation_code + "</li>" + "<br>")
        self.driver.find_element_by_id(SignUppageElement.invitation_code_field).send_keys(SignUpData.invitation_code)
        print("<li>" + "Click on Create Account button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(SignUppageElement.create_account_button).click()
        # Wait till alert is present
        alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        # Switch the control to the Alert window
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        # prompt_message = registration_prompt.text
        # print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        registration_prompt.accept()
        # Assert Navigate to Login Page
        wait_login_page = EC.presence_of_element_located((By.CLASS_NAME, LogInElement.login_button))
        WebDriverWait(self.driver, 20).until(wait_login_page)
        # Login with registered username and password
        print("<li>" + "Insert Username: " + SignUpData.new_username + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.username_field).send_keys(SignUpData.new_username)
        print("<li>" + "Insert Password: " + SignUpData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.password_field).send_keys(SignUpData.password)
        print("<li>" + "Click on Log in button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(LogInElement.login_button).click()
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        # Assert
        deposit_button = self.driver.find_element_by_class_name(MainpageElement.deposit_button).is_displayed()
        self.assertTrue(deposit_button, "User is not able to login to main page with registered username and password.")


if __name__ == '__main__':
    unittest.main()
