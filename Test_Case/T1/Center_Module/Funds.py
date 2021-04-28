import unittest
from selenium.webdriver import ActionChains
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Elements.T1.center_page import FundsElement
from Input_Data.T1.center_page import FundsData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CenterFundsModule(Base_Setup.BSetup):

    def TC_Center_Funds_01_Deposit_Amount(self):
        print("<b> Expected Results: Able to make deposit to the account. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Funds(self)
        print("<li>" + "Click on Deposit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.deposit_button).click()
        wait_page_load = EC.presence_of_element_located((By.CSS_SELECTOR, FundsElement.deposit_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        deposit_page = self.driver.find_element_by_css_selector(FundsElement.deposit_page_title).text
        self.assertEqual(deposit_page, "Deposit", "Not able to access Deposit Page")
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on Enter Amount Dropdown" + "</li>" + "<br>")
        wait_dropdown_enteramount = EC.presence_of_element_located((By.CLASS_NAME, FundsElement.deposit_form))
        WebDriverWait(self.driver, 20).until(wait_dropdown_enteramount)
        # wait_clickable_enteramount = EC.element_to_be_clickable((By.ID, FundsElement.enter_amount_dropdown))
        # WebDriverWait(self.driver, 20).until(wait_clickable_enteramount)
        self.driver.find_element_by_xpath(FundsElement.enter_amount_dropdown).click()
        print("<li>" + "Insert amount: " + FundsData.deposit_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(FundsElement.deposit_amount_field).send_keys(FundsData.deposit_amount)
        print("<li>" + "Click on Payment Overview Dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(FundsElement.payment_overview_dropdown).click()
        scroll_down = self.driver.find_element_by_xpath(FundsElement.deposit_confirm_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_down).perform()
        self.driver.implicitly_wait(10)
        wait_dropdown_paymentoverview = EC.presence_of_element_located((By.XPATH, FundsElement.deposit_confirm_button))
        WebDriverWait(self.driver, 20).until(wait_dropdown_paymentoverview)
        # will_be_charged_amount = self.driver.find_element_by_css_selector(FundsElement.will_be_charged_amount).text
        # print(will_be_charged_amount)
        # self.assertEqual(will_be_charged_amount, FundsData.deposit_amount, "Unable to insert Deposit Amount")
        print("<li>" + "Click on Confirm button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(FundsElement.deposit_confirm_button).click()
        wait_submit_modal_dialog = EC.element_to_be_clickable((By.CSS_SELECTOR, FundsElement.bank_details_confirm_button))
        WebDriverWait(self.driver, 10).until(wait_submit_modal_dialog)
        bank_details_modal_dialog = self.driver.find_element_by_css_selector(FundsElement.bank_details_confirm_button).is_displayed()
        self.assertTrue(bank_details_modal_dialog, "Unable to perform deposit.")

    def TC_Center_Funds_02_Deposit_View_All_Transactions(self):
        print("<b> Expected Results: Able to view all the deposit transaction history. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Funds(self)
        print("<li>" + "Click on Deposit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.deposit_button).click()
        wait_page_load = EC.presence_of_element_located((By.CSS_SELECTOR, FundsElement.deposit_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        deposit_page = self.driver.find_element_by_css_selector(FundsElement.deposit_page_title).text
        self.assertEqual(deposit_page, "Deposit",  "Not able to access Deposit Page")
        print("<li>" + "Click on 'See all transaction'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.deposit_see_all_transaction).click()
        wait_transpage_load = EC.presence_of_element_located((By.CLASS_NAME, FundsElement.transaction_page_navigator))
        WebDriverWait(self.driver, 20).until(wait_transpage_load)
        deposit_transpage = self.driver.find_element_by_css_selector(FundsElement.deposit_transaction_page_title).text
        self.assertEqual(deposit_transpage, "Latest Deposit", "Not able to access Deposit Transaction Page")
        self.driver.implicitly_wait(30)

    def TC_Center_Funds_03_Withdraw_Amount(self):
        print("<b> Expected Results: Able to perform withdrawal from the account. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Funds(self)
        print("<li>" + "Click on Withdraw button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.withdraw_button).click()
        wait_page_load = EC.presence_of_element_located((By.CSS_SELECTOR, FundsElement.withdraw_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        withdraw_page = self.driver.find_element_by_css_selector(FundsElement.withdraw_page_title).text
        self.assertEqual(withdraw_page, "Withdraw", "Not able to access Withdraw Page")
        print("<li>" + "Click on Withdraw button" + "</li>" + "<br>")
        self.driver.find_element_by_id(FundsElement.withdraw_amount_field).send_keys(FundsData.withdraw_amount)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.withdraw_submit_button).click()

    def TC_Center_Funds_04_Withdraw_View_All_Transactions(self):
        print("<b> Expected Results: Able to view all the withdraw transaction history. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Funds(self)
        print("<li>" + "Click on Withdraw button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.withdraw_button).click()
        wait_page_load = EC.presence_of_element_located((By.CSS_SELECTOR, FundsElement.withdraw_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        withdraw_page = self.driver.find_element_by_css_selector(FundsElement.withdraw_page_title).text
        self.assertEqual(withdraw_page, "Withdraw",  "Not able to access Withdraw Page")
        print("<li>" + "Click on 'See all transaction'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.withdraw_see_all_transaction).click()
        wait_transpage_load = EC.presence_of_element_located((By.CLASS_NAME, FundsElement.transaction_page_navigator))
        WebDriverWait(self.driver, 20).until(wait_transpage_load)
        withdraw_transpage = self.driver.find_element_by_css_selector(FundsElement.withdraw_transaction_page_title).text
        self.assertEqual(withdraw_transpage, "Latest Withdrawal", "Not able to access Withdrawal Transaction Page")
        self.driver.implicitly_wait(30)

    def test_TC_Center_Funds_05_Platform_Transfer(self):
        print("<b> Expected Results: Able to make platform transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Center_Funds(self)
        print("<li>" + "Click on Transfer button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.transfer_button).click()
        wait_page_load = EC.presence_of_element_located((By.XPATH, FundsElement.transfer_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        withdraw_page = self.driver.find_element_by_xpath(FundsElement.transfer_page_title).text
        self.assertEqual(withdraw_page, "PLATFORM TRANSFER", "Not able to access Transfer Page")
        print("<li>" + "Select 'From': " + "Main Wallet" + "</li>" + "<br>")
        wait_form_load = EC.element_to_be_clickable((By.XPATH, FundsElement.transfer_from_field))
        WebDriverWait(self.driver, 20).until(wait_form_load)
        self.driver.find_element_by_xpath(FundsElement.transfer_from_field).click()
        select_main_wallet = Select(self.driver.find_element_by_xpath(FundsElement.transfer_from_field))
        select_main_wallet.select_by_value("ZHU")
        print("<li>" + "Select 'To': " + "Evolution Gaming" + "</li>" + "<br>")
        select_main_wallet = Select(self.driver.find_element_by_xpath(FundsElement.transfer_to_field))
        select_main_wallet.select_by_value("EVO")
        print("<li>" + "Insert Amount: " + FundsData.transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(FundsElement.transfer_amount_field).send_keys(FundsData.transfer_amount)
        wait_ini_amount = EC.text_to_be_present_in_element((By.CSS_SELECTOR, FundsElement.evo_amount), "RM 0.00")
        WebDriverWait(self.driver, 20).until_not(wait_ini_amount)
        ini_main_wallet = self.driver.find_element_by_css_selector(FundsElement.main_wallet_amount).text
        ini_evo = self.driver.find_element_by_css_selector(FundsElement.evo_amount).text
        print(ini_main_wallet + "<br>")
        print(ini_evo + "<br>")
        # Assert
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(FundsElement.submit_button).click()
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
        self.driver.implicitly_wait(10)
        wait_ini_amount = EC.text_to_be_present_in_element((By.CSS_SELECTOR, FundsElement.evo_amount), "RM 0.00")
        WebDriverWait(self.driver, 20).until_not(wait_ini_amount)
        final_main_wallet = self.driver.find_element_by_css_selector(FundsElement.main_wallet_amount).text
        final_evo = self.driver.find_element_by_css_selector(FundsElement.evo_amount).text
        print(final_main_wallet + "<br>")
        print(final_evo + "<br>")
        # Assert
        self.assertTrue(ini_main_wallet < final_main_wallet, "Unable to perform platform transfer.")
        self.assertTrue(final_evo > ini_evo, "Unable to perform platform transfer.")

if __name__ == '__main__':
    unittest.main()
