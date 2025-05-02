
import unittest
from gui_game import GUIGame
from player import Player

class TestGUIGame(unittest.TestCase):
    def test_reset_game_clears_board(self):
        p1 = Player("A", "X")
        p2 = Player("B", "O")
        game = GUIGame(p1, p2, None)
        game.board.mark_square(1, 1, "X")
        game.reset_game()
        for row in game.board.grid:
            for cell in row:
                self.assertEqual(cell, "")

if __name__ == "__main__":
    unittest.main()
