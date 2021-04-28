import unittest
import HtmlTestRunner
import shutil
from Setup.T1.Base_Setup import BSetup
from Input_Data.T1.Browser import TestEvidencePath
from Test_Case.T1 import Main_Module
from Test_Case.T1 import Sign_Up_Module
from Test_Case.T1 import Login_Module
from Test_Case.T1.All_Slot_Games_Module import All_Slot_Games_Module
from Test_Case.T1.All_Live_Games_Module import All_Live_Games_Module
from Test_Case.T1.All_Sport_Games_Module import All_Sport_Games_Module
from Test_Case.T1 import Promotion_Module
from Test_Case.T1.Providers_Module.SBO import SBO
from Test_Case.T1.Providers_Module.Big_Gaming import Big_Gaming
from Test_Case.T1.Providers_Module.CMD import CMD
from Test_Case.T1.Providers_Module.Evolution_Gaming import Evolution_Gaming
from Test_Case.T1.Providers_Module.IBC import IBC
from Test_Case.T1.Providers_Module.IGS import IGS
from Test_Case.T1.Providers_Module.Spade_Gaming import Spade_Gaming
from Test_Case.T1.Providers_Module.NextSpin import NextSpin
from Test_Case.T1.Providers_Module.M8_Sports import M8_Sports
from Test_Case.T1.Providers_Module.WM_Casino import WM_Casino
from Test_Case.T1.Center_Module import Funds
from Test_Case.T1.Center_Module import Account
from Test_Case.T1.Center_Module import Referrer
from Test_Case.T1.Center_Module import Notification


# Get all tests
suite_01 = unittest.TestLoader().loadTestsFromTestCase(Main_Module.MainModule)
suite_02 = unittest.TestLoader().loadTestsFromTestCase(Sign_Up_Module.SignUpModule)
suite_03 = unittest.TestLoader().loadTestsFromTestCase(Login_Module.LoginModule)
suite_04 = unittest.TestLoader().loadTestsFromTestCase(All_Slot_Games_Module.AllSlotGamesModule)
suite_05 = unittest.TestLoader().loadTestsFromTestCase(All_Live_Games_Module.AllLiveGamesModule)
suite_06 = unittest.TestLoader().loadTestsFromTestCase(All_Sport_Games_Module.AllSportGamesModule)
suite_07 = unittest.TestLoader().loadTestsFromTestCase(Promotion_Module.PromotionModule)
suite_08_01 = unittest.TestLoader().loadTestsFromTestCase(SBO.ProvidersSBOModule)
suite_08_02 = unittest.TestLoader().loadTestsFromTestCase(Big_Gaming.ProvidersBIGModule)
suite_08_03 = unittest.TestLoader().loadTestsFromTestCase(CMD.ProvidersCMDModule)
suite_08_04 = unittest.TestLoader().loadTestsFromTestCase(Evolution_Gaming.ProvidersEVOModule)
suite_08_05 = unittest.TestLoader().loadTestsFromTestCase(IBC.ProvidersIBCModule)
suite_08_06 = unittest.TestLoader().loadTestsFromTestCase(IGS.ProvidersIGSModule)
suite_08_07 = unittest.TestLoader().loadTestsFromTestCase(Spade_Gaming.ProvidersSPAModule)
suite_08_08 = unittest.TestLoader().loadTestsFromTestCase(NextSpin.ProvidersNextSpinModule)
suite_08_09 = unittest.TestLoader().loadTestsFromTestCase(M8_Sports.ProvidersM8Module)
suite_08_10 = unittest.TestLoader().loadTestsFromTestCase(WM_Casino.ProvidersWMModule)
suite_09_01 = unittest.TestLoader().loadTestsFromTestCase(Funds.CenterFundsModule)
suite_09_02 = unittest.TestLoader().loadTestsFromTestCase(Account.CenterAccountModule)
suite_09_03 = unittest.TestLoader().loadTestsFromTestCase(Referrer.CenterReferrerModule)
suite_09_04 = unittest.TestLoader().loadTestsFromTestCase(Notification.CenterNotificationModule)


# Create test suites
Test = unittest.TestSuite(suite_04)

# Generate test report
report = TestEvidencePath.report_path


html_runner = HtmlTestRunner.HTMLTestRunner(
    output=report,
    report_title='MCIT-Frontend Test Report',
    report_name='FrontendT1_Test_Report',
    combine_reports=True,
    )

# run the test suites
html_runner.run(Test)

# Remove test evidence Folder
shutil.rmtree(BSetup.screenshot_path)
