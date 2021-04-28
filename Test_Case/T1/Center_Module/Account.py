import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.center_page import AccountElement
from Input_Data.T1.center_page import AccountData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CenterAccountModule(Base_Setup.BSetup):

    def test_TC_Center_Account_01_Edit_Account_Name(self):
        print("<b> Expected Results: Able to edit account name. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Account(self)
        wait_acc_form = EC.element_to_be_clickable((By.ID, AccountElement.name_field))
        WebDriverWait(self.driver, 10).until(wait_acc_form)
        print("<li>" + "Edit Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(AccountElement.name_field).clear()
        self.driver.find_element_by_id(AccountElement.name_field).send_keys(AccountData.edit_name)
        print("<li>" + "Click on Save changes button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(AccountElement.save_changes_button).click()
        # Wait for success alert
        # Switch the control to the Alert window
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        submit_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = submit_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        submit_prompt.accept()
        print("<li>" + "Refresh the page" + "</li>" + "<br>")
        self.driver.refresh()
        edited_name = self.driver.find_element_by_id(AccountElement.name_field).text
        print(edited_name + "<br>")
        self.assertEqual(prompt_message, "success" , "User is not able to edit name.")

        # Change back the name to ori name
        print("<li>" + "Edit Name Back to Wendy8888" + "</li>" + "<br>")
        self.driver.find_element_by_id(AccountElement.name_field).clear()
        self.driver.find_element_by_id(AccountElement.name_field).send_keys(AccountData.ori_name)
        print("<li>" + "Click on Save changes button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(AccountElement.save_changes_button).click()
        # Wait for success alert
        # Switch the control to the Alert window
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        submit_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = submit_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        submit_prompt.accept()
        print("<li>" + "Refresh the page" + "</li>" + "<br>")
        self.driver.refresh()
        ori_name = self.driver.find_element_by_id(AccountElement.name_field).text
        print(ori_name + "<br>")
        self.assertEqual(prompt_message, "success" , "User is not able to edit back name.")


if __name__ == '__main__':
    unittest.main()
