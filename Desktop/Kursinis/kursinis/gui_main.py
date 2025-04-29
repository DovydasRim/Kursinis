
import tkinter as tk
from tkinter import messagebox, simpledialog
from kursinis.gui_game import GUIGame
from kursinis.player import Player
from kursinis.ai_player import AIPlayer
from kursinis.file_handler import load_results

NO_RESULTS_TEXT = "Nėra rezultatų."

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Pagrindinis Meniu")
        master.geometry("350x300")
        try:
            master.iconbitmap("app_icon.ico")
        except:
            pass
        master.configure(bg="#d0f0f0")
        self.main_frame = tk.Frame(master, bg="#d0f0f0")
        self.main_frame.pack(pady=50)

        self.label = tk.Label(self.main_frame, text="Tic Tac Toe", font=("Helvetica", 24), bg="#d0f0f0")
        self.label.pack(pady=10)

        self.pvp_button = tk.Button(self.main_frame, text="Žaidėjas prieš žaidėją", width=25, command=self.start_pvp)
        self.pvp_button.pack(pady=5)

        self.pve_button = tk.Button(self.main_frame, text="Žaidėjas prieš kompiuterį", width=25, command=self.ask_difficulty)
        self.pve_button.pack(pady=5)

        self.results_button = tk.Button(self.main_frame, text="Paskutinių 5 žaidimų rezultatai", width=25, command=self.show_results)
        self.results_button.pack(pady=5)

    def start_pvp(self):
        name1 = simpledialog.askstring("Žaidėjas 1", "Įveskite pirmo žaidėjo vardą:")
        name2 = simpledialog.askstring("Žaidėjas 2", "Įveskite antro žaidėjo vardą:")
        if not name1 or not name2:
            messagebox.showerror("Klaida", "Būtina įvesti abiejų žaidėjų vardus!")
            return

        self.new_window()
        player1 = Player(name1, "X")
        player2 = Player(name2, "O")
        game = GUIGame(player1, player2, self.master)
        game.play()

    def ask_difficulty(self):
        self.difficulty_window = tk.Toplevel(self.master)
        self.difficulty_window.title("Pasirinkite AI lygį")
        self.difficulty_window.configure(bg="#d0f0f0")
        try:
            self.difficulty_window.iconbitmap("app_icon.ico")
        except:
            pass

        label = tk.Label(self.difficulty_window, text="Pasirinkite AI sudėtingumą:", bg="#d0f0f0", font=("Helvetica", 14))
        label.pack(pady=10)

        easy_button = tk.Button(self.difficulty_window, text="Lengvas", width=20, command=lambda: self.start_pve("easy"))
        easy_button.pack(pady=5)

        hard_button = tk.Button(self.difficulty_window, text="Sunkus", width=20, command=lambda: self.start_pve("hard"))
        hard_button.pack(pady=5)

    def start_pve(self, difficulty):
        self.difficulty_window.destroy()
        name1 = simpledialog.askstring("Žaidėjas", "Įveskite savo vardą:")
        if not name1:
            messagebox.showerror("Klaida", "Būtina įvesti žaidėjo vardą!")
            return

        self.new_window()
        player1 = Player(name1, "X")
        player2 = AIPlayer("O", difficulty=difficulty)
        game = GUIGame(player1, player2, self.master)
        game.play()

    def show_results(self):
        results = load_results()
        result_window = tk.Toplevel(self.master)
        result_window.title("Paskutiniai 5 rezultatai")
        result_window.geometry("350x300")
        try:
            result_window.iconbitmap("app_icon.ico")
        except Exception as e:
            print(f"Warning: Unable to set iconbitmap. Error: {e}")
        result_window.configure(bg="#d0f0f0")

        if results:
            label = tk.Label(result_window, text="Paskutiniai 5 rezultatai:", bg="#d0f0f0", font=("Helvetica", 14))
            label.pack(pady=10)
            header = tk.Label(result_window, text="Žaidėjas nr. 1 | Žaidėjas nr. 2 | Nugalėtojas", bg="#d0f0f0", font=("Helvetica", 10, "bold"))
            header.pack(pady=(0, 5))

            for res in results[-5:]:
                display_text = " | ".join(str(item) for item in res)
                label = tk.Label(result_window, text=display_text, bg="#d0f0f0")
                label.pack()
        else:
            label = tk.Label(result_window, text=NO_RESULTS_TEXT, bg="#d0f0f0")
            label.pack()

    def new_window(self):
        self.master.withdraw()

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
