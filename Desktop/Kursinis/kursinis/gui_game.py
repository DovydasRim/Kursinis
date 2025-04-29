
import pygame
import sys
import os
import tkinter as tk
from tkinter import messagebox
import time
from kursinis.board import Board
from kursinis.ai_player import AIPlayer
from kursinis.player import Player
from kursinis.file_handler import save_result

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
WIN_LINE_COLOR = (255, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

screen.fill(BG_COLOR)

sound_x = pygame.mixer.Sound(resource_path('sounds/place_x.mp3'))
sound_o = pygame.mixer.Sound(resource_path('sounds/place_o.mp3'))
sound_win = pygame.mixer.Sound(resource_path('sounds/win.mp3'))
sound_draw = pygame.mixer.Sound(resource_path('sounds/draw.mp3'))

class GUIGame:
    def __init__(self, player1, player2, master):
        self.master = master
    
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.running = True
        self.win_info = None
        self.start_time = None
        self.draw_lines()

    def draw_lines(self):
        if not pygame.display.get_init():
            return
        screen.fill(BG_COLOR)
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

    def draw_win_line(self):
        if not self.win_info:
            return

        kind = self.win_info[0]
        if kind == "horizontal":
            row = self.win_info[1]
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.line(screen, WIN_LINE_COLOR, (20, y), (WIDTH - 20, y), 10)
        elif kind == "vertical":
            col = self.win_info[1]
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            pygame.draw.line(screen, WIN_LINE_COLOR, (x, 20), (x, HEIGHT - 20), 10)
        elif kind == "desc_diagonal":
            pygame.draw.line(screen, WIN_LINE_COLOR, (20, 20), (WIDTH - 20, HEIGHT - 20), 10)
        elif kind == "asc_diagonal":
            pygame.draw.line(screen, WIN_LINE_COLOR, (20, HEIGHT - 20), (WIDTH - 20, 20), 10)

    def reset_game(self):
        self.board.reset()
        self.running = True
        self.current_player = self.player1
        self.win_info = None
        self.start_time = time.time()
        self.draw_lines()
        pygame.display.update()

    def play(self):
        self.reset_game()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and self.running:
                    if not isinstance(self.current_player, AIPlayer):
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        clicked_row = mouseY // SQUARE_SIZE
                        clicked_col = mouseX // SQUARE_SIZE

                        if self.board.available_square(clicked_row, clicked_col):
                            self.make_move(clicked_row, clicked_col)

            if self.running and isinstance(self.current_player, AIPlayer):
                pygame.time.delay(750)
                
                row, col = self.current_player.get_move(self.board)
                if row is not None and col is not None:
                    self.make_move(row, col)

            self.draw_lines()
            self.draw_figures()
            self.draw_win_line()
            pygame.display.update()
            clock.tick(30)

    
    
    def make_move(self, row, col):
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, self.current_player.symbol)

            if self.current_player.symbol == "X":
                sound_x.play()
            else:
                sound_o.play()

            win_result = self.board.check_win(self.current_player.symbol)
            if win_result:
                self.running = False
                self.win_info = win_result
                save_result(self.player1.name, self.player2.name, f"{self.current_player.name} laimėjo")
                sound_win.play()

                self.draw_lines()
                self.draw_figures()
                self.draw_win_line()
                pygame.display.update()
                pygame.time.delay(800)

                self.end_game_message(f"{self.current_player.name} laimėjo! 🎉")
                return

            elif self.board.is_full():
                self.running = False
                save_result(self.player1.name, self.player2.name, "Lygiosios")
                sound_draw.play()

                self.draw_lines()
                self.draw_figures()
                self.draw_win_line()
                pygame.display.update()
                pygame.time.delay(800)

                self.end_game_message("Žaidimas baigėsi lygiosiomis! 🤝")
                return
            else:
                self.switch_player()
                self.draw_lines()
                self.draw_figures()
                self.draw_win_line()
                pygame.display.update()


    def end_game_message(self, result_text):
        total_time = int(time.time() - self.start_time)
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Žaidimo pabaiga", "{} Žaidimas truko {} sek.".format(result_text, total_time)
)
        self.master.deiconify()
        self.game_active = False
        pygame.quit()


    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
