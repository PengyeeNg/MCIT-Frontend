import unittest
from Setup.T1 import Base_Setup
from Actions.T1.allslotgames_page import AllSlotGamesActions
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions

class AllSlotGamesModule(Base_Setup.BSetup):

    def test_TC_AllSlotGames_01_Navigate_to_RespinMania_Login(self):
        print("<b> Expected Results: Access to RespinMania Page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        AllSlotGamesActions.Navigate_to_RespinMania(self)
        # Assert
        AllSlotGamesActions.Assert_Quick_Transfer_Modal_Dialog(self)


    def test_TC_AllSlotGames_02_Navigate_to_RespinMania_UnLogin(self):
        print("<b> Expected Results: Access to Login Page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        AllSlotGamesActions.Navigate_to_JinFuXingYun(self)
        AllSlotGamesActions.Navigate_back_to_LoginPage(self)


if __name__ == '__main__':
    unittest.main()

