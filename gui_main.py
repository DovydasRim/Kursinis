from player import Player
from ai_player import AIPlayer
from gui_game import GUIGame

def setup_players():
    mode = input("Play with (1) another player or (2) AI? ")
    if mode == "2":
        return Player("You", "X"), AIPlayer("O")
    else:
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        return Player(name1, "X"), Player(name2, "O")

def main():
    player1, player2 = setup_players()
    game = GUIGame(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
