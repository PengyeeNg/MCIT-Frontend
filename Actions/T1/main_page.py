from selenium.webdriver import ActionChains

from Setup.T1 import Base_Setup
from Input_Data.T1.Browser import BrowserData
from Elements.T1.main_page import MainpageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Elements.T1.center_page import ReferrerElement


class MainpageActions(Base_Setup.BSetup):

    def Access_to_Mainpage(self):
        print("<li>" + "Access to Frontend T1 Webpage: " + BrowserData.webpage_t1 + "</li>" + "<br>")
        self.driver.get(BrowserData.webpage_t1)
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        # Assert
        main_page = self.driver.title
        self.assertEqual(main_page, "Platform","User is not able to access to main page.")

    def Access_to_Login_Page(self):
        print("<li>" + "Click on Login button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.login_button).click()
        # Wait the page loads
        wait_login_page = EC.presence_of_element_located((By.ID, MainpageElement.username_field))
        WebDriverWait(self.driver, 20).until(wait_login_page)
        # Assert
        login_page_element = self.driver.find_element_by_id(MainpageElement.username_field).is_displayed()
        self.assertTrue(login_page_element, "User is not able to access to login page.")

    def Access_to_SignUp_Page(self):
        print("<li>" + "Click on Sign Up button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.sign_up_button).click()
        # Wait the page loads
        wait_signup_page = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.create_account_button))
        WebDriverWait(self.driver, 20).until(wait_signup_page)
        # Assert
        signup_page_element = self.driver.find_element_by_class_name(MainpageElement.create_account_button).is_displayed()
        self.assertTrue(signup_page_element, "User is not able to access to sign up page.")

    def Access_to_AllSlotGames_Page(self):
        print("<li>" + "Click on All Slot games" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.all_slot_games_button).click()
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # Assert
        game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
        self.assertTrue(game_page_element, "User is not able to access to All Slot Games page.")

    def Access_to_AllLiveGames_Page(self):
        print("<li>" + "Click on All Live games" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.all_live_games_button).click()
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # Assert
        game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
        self.assertTrue(game_page_element, "User is not able to access to All Live Games page.")

    def Access_to_AllSportGames_Page(self):
        print("<li>" + "Click on All Live games" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.all_sport_games_button).click()
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # Assert
        game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
        self.assertTrue(game_page_element, "User is not able to access to All Sport Games page.")

    def Access_to_Promotion_Page(self):
        print("<li>" + "Click on Promotion" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.promotion_button).click()
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # Assert
        game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
        self.assertTrue(game_page_element, "User is not able to access to Promotion page.")

    def Access_to_Providers_Page(self):
        print("<li>" + "Click on Providers" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.providers_button).click()
        # Wait the page loads
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # Assert
        game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
        self.assertTrue(game_page_element, "User is not able to access to Providers page.")

    def Access_to_Center_Funds(self):
        dropdown_expanded = self.driver.find_element_by_xpath(MainpageElement.center_funds_button).is_displayed()
        if dropdown_expanded is True:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            print("<li>" + "Click on Funds" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_funds_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Funds page.")
        else:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_button).click()
            # Wait dropdown displays
            wait_dropdown = EC.presence_of_element_located((By.XPATH, MainpageElement.center_funds_button))
            WebDriverWait(self.driver, 10).until(wait_dropdown)
            # Select Funds
            print("<li>" + "Click on Funds" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_funds_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Funds page.")

    def Access_to_Center_Account(self):
        dropdown_expanded = self.driver.find_element_by_xpath(MainpageElement.center_account_button).is_displayed()
        if dropdown_expanded is True:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            print("<li>" + "Click on Account" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_account_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Account page.")
        else:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_button).click()
            # Wait dropdown displays
            wait_dropdown = EC.presence_of_element_located((By.XPATH, MainpageElement.center_account_button))
            WebDriverWait(self.driver, 10).until(wait_dropdown)
            # Select Account
            print("<li>" + "Click on Account" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_account_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Account page.")

    def Access_to_Center_Referrer(self):
        dropdown_expanded = self.driver.find_element_by_xpath(MainpageElement.center_referrer_button).is_displayed()
        if dropdown_expanded is True:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            print("<li>" + "Click on Referrer" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_referrer_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Referrer page.")
        else:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_button).click()
            # Wait dropdown displays
            wait_dropdown = EC.presence_of_element_located((By.XPATH, MainpageElement.center_referrer_button))
            WebDriverWait(self.driver, 10).until(wait_dropdown)
            scroll_down = self.driver.find_element_by_class_name(ReferrerElement.logout_button)
            actions = ActionChains(self.driver)
            actions.move_to_element(scroll_down).perform()
            self.driver.implicitly_wait(10)
            # Select Referrer
            print("<li>" + "Click on Referrer" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_referrer_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Referrer page.")

    def Access_to_Center_Notification(self):
        dropdown_expanded = self.driver.find_element_by_xpath(MainpageElement.center_notification_button).is_displayed()
        if dropdown_expanded is True:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            print("<li>" + "Click on Notification" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_notification_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Referrer page.")
        else:
            print("<li>" + "Click on Center" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_button).click()
            # Wait dropdown displays
            wait_dropdown = EC.presence_of_element_located((By.XPATH, MainpageElement.center_notification_button))
            WebDriverWait(self.driver, 10).until(wait_dropdown)
            scroll_down = self.driver.find_element_by_class_name(ReferrerElement.logout_button)
            actions = ActionChains(self.driver)
            actions.move_to_element(scroll_down).perform()
            self.driver.implicitly_wait(10)
            # Select Referrer
            print("<li>" + "Click on Notification" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(MainpageElement.center_referrer_button).click()
            # Wait page load
            wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.games_title))
            WebDriverWait(self.driver, 20).until(wait_page_load)
            # Assert
            game_page_element = self.driver.find_element_by_class_name(MainpageElement.games_title).is_displayed()
            self.assertTrue(game_page_element, "User is not able to access to Center-Referrer page.")


