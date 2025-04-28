class Board:
    def __init__(self):
        self.grid = [["" for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print(" | ".join(cell if cell else " " for cell in row))
            print("-" * 5)

    def update_move(self, row, col, symbol):
        if self.grid[row][col] == "":
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
        if all(self.grid[i][i] == symbol for i in range(3)) or all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(all(cell != "" for cell in row) for row in self.grid)

    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.grid[i][j] == ""]
