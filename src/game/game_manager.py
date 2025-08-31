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

    def next_turn(self):
        """
        Setea el siguiente jugador (dentro de la misma ronda)

        Returns:
            None
        """
        self.current_player = (self.current_player + 1) % self.player_quantity

