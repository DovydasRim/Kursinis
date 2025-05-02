
import unittest
from ai_player import AIPlayer
from board import Board

class TestAIPlayerRobust(unittest.TestCase):
    def test_ai_avoids_taken_squares(self):
        board = Board()
        board.mark_square(0, 0, "X")
        ai = AIPlayer("Bot", "O")
        row, col = ai.get_move(board)
        self.assertNotEqual((row, col), (0, 0))

if __name__ == "__main__":
    unittest.main()
