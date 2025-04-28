from board import Board
from player import Player
from ai_player import AIPlayer
from file_handler import save_result

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play_turn(self):
        while True:
            row, col = self.current_player.get_move(self.board)
            if self.board.update_move(row, col, self.current_player.symbol):
                break
            else:
                print("Invalid move, try again.")

    def start_game(self):
        while True:
            self.board.display()
            self.play_turn()
            if self.board.check_win(self.current_player.symbol):
                self.board.display()
                print(f"{self.current_player.name} wins!")
                save_result(self.player1.name, self.player2.name, self.current_player.name)
                return self.current_player.name
            elif self.board.check_draw():
                self.board.display()
                print("It's a draw!")
                save_result(self.player1.name, self.player2.name, "Draw")
                return "Draw"
            self.switch_player()
