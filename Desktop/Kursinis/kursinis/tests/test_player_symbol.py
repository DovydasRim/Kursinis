
import unittest
from player import Player

class TestPlayerSymbol(unittest.TestCase):
    def test_symbol_assignment(self):
        p = Player("Jonas", "X")
        self.assertEqual(p.symbol, "X")
        self.assertNotEqual(p.symbol, "O")

if __name__ == "__main__":
    unittest.main()
