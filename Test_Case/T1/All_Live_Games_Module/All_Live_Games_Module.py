import unittest
from Setup.T1 import Base_Setup
from Actions.T1.alllivegames_page import AllLiveGamesActions


class AllLiveGamesModule(Base_Setup.BSetup):

    def test_TC_AllLiveGames_01_Access_to_3CardBragLive(self):
        print("<b> Expected Results: Access to 3 Card Brag Live Page. </b>" + "<br>")
        AllLiveGamesActions.Navigate_to_3CardBragLive(self)
        # Assert
        AllLiveGamesActions.Assert_Quick_Transfer_Modal_Dialog(self)


if __name__ == '__main__':
    unittest.main()
