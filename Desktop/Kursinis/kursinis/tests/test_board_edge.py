
import unittest
from board import Board

class TestBoardEdgeCases(unittest.TestCase):
    def test_prevent_overwrite(self):
        board = Board()
        board.mark_square(0, 0, "X")
        board.mark_square(0, 0, "O")  # turėtų ignoruoti
        self.assertEqual(board.grid[0][0], "X")

if __name__ == "__main__":
    unittest.main()
