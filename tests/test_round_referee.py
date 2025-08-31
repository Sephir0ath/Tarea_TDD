import unittest
from src.game.round_referee import RoundReferee
from src.game.game_manager import GameManager

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRoundReferee(unittest.TestCase):
    def setUp(self):
        self.referee = RoundReferee()
        self.player_quantity = 4
        self.manager = GameManager(self.player_quantity)

        self.manager.initial_player = 2
        self.manager.current_player = 2

    def test_arbitro_maneja_dudo(self):
        for player in self.manager.players:
            for dice in player.dices:
                dice.value = 3

        # Pierde un dado el jugador anterior ya que solo hay trenes en los cachos
        self.referee.current_bet = (2, 2)
        self.referee.handle_doubt(self.manager.players, self.manager.current_player) # Pierde el jugador que hizo la apuesta (el anterior al actual)

        last_player = self.manager.players[(self.manager.current_player - 1) % self.player_quantity]
        self.assertEqual(len(last_player.get_dices()),  4) # Obtenemos la cantidad de dados que tiene actualmente el jugador anterior que hizo la apuesta

        # Pierde el jugador actual ya que hay al menos 4 trenes en total
        self.referee.current_bet = (4, 3)
        self.referee.handle_doubt(self.manager.players, self.manager.current_player)
        current_player = self.manager.players[self.manager.current_player]
        self.assertEqual(len(current_player.get_dices()), 4)

