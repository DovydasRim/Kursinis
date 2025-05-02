
import random
from kursinis.board import Board

class AIPlayer:
    def __init__(self, symbol, difficulty="easy"):
        self.name = "Kompiuteris"
        self.symbol = symbol
        self.difficulty = difficulty

    def get_move(self, board):
        if self.difficulty == "hard":
            opponent_symbol = "O" if self.symbol == "X" else "X"
            for r in range(3):
                for c in range(3):
                    if board.available_square(r, c):
                        board.grid[r][c] = opponent_symbol
                        if board.check_win(opponent_symbol):
                            board.grid[r][c] = ""
                            return (r, c)
                        board.grid[r][c] = ""

        empty_squares = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == ""]
        return random.choice(empty_squares) if empty_squares else None
