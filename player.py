class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        row = int(input(f"{self.name}, enter row (0-2): "))
        col = int(input(f"{self.name}, enter column (0-2): "))
        return row, col
