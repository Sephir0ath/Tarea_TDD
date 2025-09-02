from .cacho import Cacho
from random import randint
from .round_referee import RoundReferee


class GameManager:
    def __init__(self, player_quantity):
        self.player_quantity = player_quantity
        self.players = []
        self.initial_player = None
        self.current_player = None
        self.total_player_quantity = player_quantity
        self.has_activated_special_round = []


        for i in range(player_quantity):
            self.players.append(Cacho())
            self.has_activated_special_round.append(False)

    def set_initial_player(self):
        """
        Setea el jugador inicial

        Returns:
            None
        """
        self.initial_player = randint(0, len(self.players)-1)
        self.current_player = self.initial_player
        return self.current_player

    def next_turn(self):
        """
        Setea el siguiente jugador (dentro de la misma ronda)

        Returns:
            None
        """
        self.current_player = (self.current_player + 1) % self.player_quantity
        return self.current_player

    def roll_dices(self):
        """
        Lanza todos los dados de todos los jugadores en la partida

        Returns:
             None
        """
        for x in self.players:
            x.roll_dices()