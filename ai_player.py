import random
from player import Player

class AIPlayer(Player):
    def __init__(self, symbol):
        super().__init__("Computer", symbol)

    def get_move(self, board):
        print(f"{self.name} is thinking...")
        empty_cells = board.get_empty_cells()
        return random.choice(empty_cells)
