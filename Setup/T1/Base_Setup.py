import base64
import unittest
import os
from datetime import datetime
from Input_Data.T1.Browser import BrowserData
from selenium import webdriver



class BSetup(unittest.TestCase):
    # Define folder's name format
    folder_date = datetime.now().strftime('%Y%m%d')
    # Define path to save test evidence
    screenshot_path = r"C:\Users\Lenovo\PycharmProjects\MCIT-Frontend\Screenshot\T1\Test_Evidence-%s" % folder_date
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)

    def setUp(self):
        # create a new Chrome session
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"popups": 1}
        self.driver = webdriver.Chrome(BrowserData.chrome_path)
        # Maximize the window
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        # Define image's name format
        test_name = self.id()
        image_date_time = datetime.now().strftime('_%H%M%S')
        # Capture test evidence with test name and timestamp
        file_name = "%s" % test_name
        evidence_id = file_name + "%s.png" % image_date_time
        name = os.path.join(BSetup.screenshot_path, evidence_id)
        self.driver.get_screenshot_as_file(name)

        # Convert test evidence into base64 format
        data_uri = base64.b64encode(open(name, 'rb').read()).decode('utf-8')
        img_tag = '<img src="data:image/png;base64,{0}" width="929" height="420">'.format(data_uri)
        # Include test evidence name and images in test report
        print("<b> Actual Results: </b>" + "<br>")
        print(img_tag)
        # print(" Test Evidence ID: " + evidence_id)
        # Close the Chrome driver
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
