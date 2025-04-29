
import random
from kursinis.board import Board

class AIPlayer:
    def __init__(self, symbol, difficulty="easy"):
        self.name = "Kompiuteris"
        self.symbol = symbol
        self.difficulty = difficulty

    def get_move(self, board):
        if self.difficulty == "hard":
            # Patikrina, ar gali užblokuoti varžovą
            opponent_symbol = "O" if self.symbol == "X" else "X"
            # Tikrina ar varžovas gali laimėti kito ėjimo metu
            for r in range(3):
                for c in range(3):
                    if board.available_square(r, c):
                        # Simuliuoja, jei varžovas įdėtų
                        board.grid[r][c] = opponent_symbol
                        if board.check_win(opponent_symbol):
                            board.grid[r][c] = ""  # Atstato
                            return (r, c)  # Blokuoti
                        board.grid[r][c] = ""  # Atstato

        # Lengvas arba nėra grėsmės: deda atsitiktinai
        empty_squares = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == ""]
        return random.choice(empty_squares) if empty_squares else None
