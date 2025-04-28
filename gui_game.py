import pygame
from board import Board
from ai_player import AIPlayer
from player import Player
from file_handler import save_result

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

class GUIGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.running = True
        self.draw_lines()

    def draw_lines(self):
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                symbol = self.board.grid[row][col]
                if symbol == 'O':
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                              int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif symbol == 'X':
                    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

    def get_mouse_click(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def make_move(self, row, col):
        if self.board.update_move(row, col, self.current_player.symbol):
            self.draw_figures()
            return True
        return False

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if isinstance(self.current_player, AIPlayer):
                    pygame.time.wait(500)
                    row, col = self.current_player.get_move(self.board)
                    self.make_move(row, col)
                    if self.board.check_win(self.current_player.symbol):
                        print(f"{self.current_player.name} wins!")
                        save_result(self.player1.name, self.player2.name, self.current_player.name)
                        self.running = False
                    elif self.board.check_draw():
                        print("Draw!")
                        save_result(self.player1.name, self.player2.name, "Draw")
                        self.running = False
                    self.switch_player()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.running:
                    row, col = self.get_mouse_click(event.pos)
                    if self.make_move(row, col):
                        if self.board.check_win(self.current_player.symbol):
                            print(f"{self.current_player.name} wins!")
                            save_result(self.player1.name, self.player2.name, self.current_player.name)
                            self.running = False
                        elif self.board.check_draw():
                            print("Draw!")
                            save_result(self.player1.name, self.player2.name, "Draw")
                            self.running = False
                        self.switch_player()
            pygame.display.update()
