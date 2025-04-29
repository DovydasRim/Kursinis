
class Board:
    def __init__(self):
        self.grid = [["" for _ in range(3)] for _ in range(3)]

    def mark_square(self, row, col, symbol):
        if self.available_square(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def available_square(self, row, col):
        return self.grid[row][col] == ""

    def is_full(self):
        return all(all(cell != "" for cell in row) for row in self.grid)

    def check_win(self, symbol):
        # Horizontal
        for r in range(3):
            if all(self.grid[r][c] == symbol for c in range(3)):
                return ("horizontal", r)
        # Vertical
        for c in range(3):
            if all(self.grid[r][c] == symbol for r in range(3)):
                return ("vertical", c)
        # Diagonal (top-left to bottom-right)
        if all(self.grid[i][i] == symbol for i in range(3)):
            return ("desc_diagonal",)
        # Diagonal (bottom-left to top-right)
        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return ("asc_diagonal",)
        return None

    def reset(self):
        self.grid = [["" for _ in range(3)] for _ in range(3)]
