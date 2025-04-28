
from player import HumanPlayer
from ai_player import AIPlayer

class PlayerFactory:
    @staticmethod
    def create_player(player_type, symbol):
        if player_type.lower() == "human":
            return HumanPlayer(symbol)
        elif player_type.lower() == "ai":
            return AIPlayer(symbol)
        else:
            raise ValueError("Unknown player type: " + player_type)
