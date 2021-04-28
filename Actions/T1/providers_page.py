from Setup.T1 import Base_Setup
from Elements.T1.providers_page import ProvidersElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.T1.providers_page import ProvidersData
from selenium.webdriver.common.action_chains import ActionChains
import requests

class ProvidersActions(Base_Setup.BSetup):

    def Assert_Quick_Transfer_Modal_Dialog(self):
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ProvidersElement.quick_transfer_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.implicitly_wait(10)
        quick_transfer = self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_button).is_displayed()
        self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not shown as expected.")

    def Quick_Transfer_Enter_Game(self):
        wait_enter_game = EC.element_to_be_clickable((By.XPATH, ProvidersElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_enter_game)
        click_enter = self.driver.find_element_by_xpath(ProvidersElement.enter_the_game_button).click()
        self.driver.implicitly_wait(10)

    def Quick_Transfer(self):
        print("<li>" + "Insert Amount: " + ProvidersData.quick_transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_amount).clear()
        empty_field = self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_amount).text
        # wait_empty = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.updated_transfer_amount), "")
        # WebDriverWait(self.driver, 20).until(wait_empty)
        self.assertEqual(empty_field, "", "Not able to clear the transfer amount field")
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_amount).send_keys(ProvidersData.quick_transfer_amount)
        # wait_empty = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.updated_transfer_amount), "0.00")
        # WebDriverWait(self.driver, 20).until(wait_empty)
        # amount_field = self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_amount).text
        # self.assertNotEqual(amount_field, "", "Not able to insert amount to the transfer amount field")
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ProvidersElement.quick_transfer_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_button).click()
        # Switch the control to the Alert window
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = registration_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        registration_prompt.accept()

    def Close_Quick_Transfer_Modal_Dialog(self):
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_cross_button).click()
        self.driver.implicitly_wait(10)

    def Assert_New_Gaming_Page(self):
        # gaming_page_title = self.driver.title
        game_url = self.driver.current_url
        r = requests.get(game_url)
        print("The gaming page status is: " + str(r.status_code) + "<br>")
        # print("The gaming page name is: " + gaming_page_title + "<br>")
        # Close the tab
        self.driver.close()

    def Providers_Close_Quick_Transfer_Modal_Dialogs(self):
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ProvidersElement.quick_transfer_cross_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_cross_button).click()
        wait_page_load = EC.invisibility_of_element_located((By.CLASS_NAME, ProvidersElement.modal_content))
        WebDriverWait(self.driver, 10).until(wait_page_load)

    def Navigate_to_Evolution_Gaming(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.evolution_gaming))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on Evolution Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.evolution_gaming).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to Evolution Gaming.")
        # Assert provider title
        wait_evo = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "Evolution Gaming")
        WebDriverWait(self.driver, 20).until(wait_evo)
        evo_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(evo_title, "Evolution Gaming", "User is not able to access to Evolution Gaming game list.")

    def Navigate_to_Spade_Gaming(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.spade_gaming))
        WebDriverWait(self.driver, 20).until(wait_page_load)

        print("<li>" + "Click on Spade Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.spade_gaming).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to Spade Gaming.")
        # Assert provider title
        wait_spa = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "Spade Gaming")
        WebDriverWait(self.driver, 20).until(wait_spa)
        spa_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(spa_title, "Spade Gaming", "User is not able to access to Spade Gaming game list.")

    def Navigate_to_CMD(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.cmd))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on CMD Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.cmd).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to CMD.")
        # Assert provider title
        wait_cmd = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "CMD")
        WebDriverWait(self.driver, 20).until(wait_cmd)
        cmd_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(cmd_title, "CMD", "User is not able to access to CMD game list.")

    def Navigate_to_SBO(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.sbo))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on SBO Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.sbo).click()
        # Assert provider title
        wait_sbo = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "SBO")
        WebDriverWait(self.driver, 20).until(wait_sbo)
        sbo_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(sbo_title, "SBO", "User is not able to access to SBO game list.")

    def Navigate_to_Big_Gaming(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.big_gaming))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on Big Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.big_gaming).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to Big Gaming.")
        # Assert provider title
        wait_big = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "Big Gaming")
        WebDriverWait(self.driver, 20).until(wait_big)
        big_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(big_title, "Big Gaming", "User is not able to access to Big Gaming game list.")

    def Navigate_to_IBC(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.ibc))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on IBC" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.ibc).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to IBC.")
        # Assert provider title
        wait_ibc = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "IBC")
        WebDriverWait(self.driver, 20).until(wait_ibc)
        ibc_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(ibc_title, "IBC", "User is not able to access to IBC game list.")

    def Navigate_to_M8_Sports(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.m8_sports))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on M8 Sports" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.m8_sports).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to M8 Sports.")
        # Assert provider title
        wait_m8 = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "M8 Sports")
        WebDriverWait(self.driver, 20).until(wait_m8)
        m8_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(m8_title, "M8 Sports", "User is not able to access to M8 Sports game list.")

    def Navigate_to_IGS(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.igs))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on IGS" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.igs).click()
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to IGS.")
        # Assert provider title
        wait_igs = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "IGS")
        WebDriverWait(self.driver, 20).until(wait_igs)
        igs_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(igs_title, "IGS", "User is not able to access to IGS game list.")

    def Navigate_to_WM_Casino(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wm_casino))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on WM Casino" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.wm_casino).click()
        scroll_up = self.driver.find_element_by_class_name(ProvidersElement.scroll_up)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_up).perform()
        self.driver.implicitly_wait(10)
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to WM Casino.")
        # Assert provider title
        wait_vm = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "WM Casino")
        WebDriverWait(self.driver, 20).until(wait_vm)
        vm_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(vm_title, "WM Casino", "User is not able to access to WM Casino game list.")

    def Navigate_to_NextSpin(self):
        # Wait the page loads
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.nextspin))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        print("<li>" + "Click on NextSpin" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.nextspin).click()
        scroll_up = self.driver.find_element_by_class_name(ProvidersElement.scroll_up)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_up).perform()
        self.driver.implicitly_wait(10)
        # Assert provider category
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.wait_page_load))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(ProvidersElement.wait_page_load).is_displayed()
        self.assertTrue(page_loaded, "Not able to access to NextSpin.")
        # Assert provider title
        wait_nextspin = EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProvidersElement.provider_title), "NextSpin")
        WebDriverWait(self.driver, 20).until(wait_nextspin)
        nextspin_title = self.driver.find_element_by_css_selector(ProvidersElement.provider_title).text
        self.assertEqual(nextspin_title, "NextSpin", "User is not able to access to NextSpin game list.")


