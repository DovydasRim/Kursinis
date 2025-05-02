
import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        p = Player("Dovydas", "X")
        self.assertEqual(p.name, "Dovydas")
        self.assertEqual(p.symbol, "X")

    def test_get_move_returns_none(self):
        p = Player("Test", "O")
        self.assertEqual(p.get_move(None), (None, None))

if __name__ == "__main__":
    unittest.main()
