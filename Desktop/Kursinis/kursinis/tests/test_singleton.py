
import unittest
from gui_game import GUIGame
from player import Player

class TestGUIGameSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        p1 = Player("A", "X")
        p2 = Player("B", "O")
        g1 = GUIGame(p1, p2, None)
        g2 = GUIGame(p1, p2, None)
        self.assertIs(g1, g2)

if __name__ == "__main__":
    unittest.main()
