import unittest
from Setup.T1 import Base_Setup
from Actions.T1.allsportgames_page import AllSportGamesActions


class AllSportGamesModule(Base_Setup.BSetup):

    def test_TC_AllSportGames_01_Navigate_to_SportsBook(self):
        print("<b> Expected Results: Access to Sports Book Page. </b>" + "<br>")
        AllSportGamesActions.Navigate_to_Sports_Book(self)
        # Assert
        AllSportGamesActions.Assert_Quick_Transfer_Modal_Dialog(self)


if __name__ == '__main__':
    unittest.main()

