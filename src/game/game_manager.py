from .cacho import Cacho
from random import randint

class GameManager:
    def __init__(self, player_quantity):
        self.player_quantity = player_quantity
        self.players = []
        self.initial_player = None

        for i in range(player_quantity):
            self.players.append(Cacho())


    def set_initial_player(self):
        """
        Setea el jugador inicial

        Returns:
            None
        """
        self.initial_player = randint(0, len(self.players)-1)

