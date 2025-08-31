import unittest

from src.game.dice import Dice
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

        for player in self.manager.players:
            for dice in player.dices:
                dice.value = 3

    def test_arbitro_maneja_dudo(self):
        # Pierde un dado el jugador anterior ya que solo hay trenes en los cachos
        self.referee.current_bet = (2, 2)
        self.referee.handle_doubt(self.manager.players, self.manager.current_player, self.manager.has_activated_special_round, self.manager.player_quantity) # Pierde el jugador que hizo la apuesta (el anterior al actual)

        last_player = self.manager.players[(self.manager.current_player - 1) % self.manager.player_quantity]
        self.assertEqual(len(last_player.get_dices()),  4) # Obtenemos la cantidad de dados que tiene actualmente el jugador anterior que hizo la apuesta

        # Pierde el jugador actual ya que hay al menos 4 trenes en total
        self.referee.current_bet = (4, 3)
        self.referee.handle_doubt(self.manager.players, self.manager.current_player, self.manager.has_activated_special_round, self.manager.player_quantity)
        current_player = self.manager.players[self.manager.current_player]
        self.assertEqual(len(current_player.get_dices()), 4)

    def test_se_remueve_jugador(self):
        self.manager.players[2].dices = [Dice()]
        self.referee.current_bet = (4, 3)

        self.referee.handle_doubt(self.manager.players, self.manager.current_player, self.manager.has_activated_special_round, self.manager.player_quantity)  # Pierde el jugador que hizo la apuesta (el anterior al actual)
        self.assertEqual(len(self.manager.players), self.player_quantity-1)

    def test_arbitro_maneja_calzo(self):
        self.referee.current_bet = (self.player_quantity*5, 3) # La cantidad exacta de trenes que están en juego
        self.referee.handle_calzo(self.manager.players, self.manager.current_player, self.manager.has_activated_special_round, self.manager.player_quantity)
        actual_player_dice_quantity = len(self.manager.players[self.manager.current_player].dices)
        self.assertEqual(actual_player_dice_quantity, 5) # El jugador no pierde dados


        self.referee.current_bet = (self.manager.player_quantity*5, 2)
        self.referee.handle_calzo(self.manager.players, self.manager.current_player, self.manager.has_activated_special_round, self.manager.player_quantity)
        actual_player_dice_quantity = len(self.manager.players[self.manager.current_player].dices)
        self.assertEqual(actual_player_dice_quantity, 4)  # El jugador pierde dado

    def test_validar_posibilidad_de_calzo(self):
        # El jugador actual no tiene un solo dado y tampoco están en juego menos de la mitad de los dados (condiciones de calzo)
        self.assertFalse(self.referee.validate_calzo(self.manager.players, self.manager.current_player, self.manager.total_player_quantity))

        self.referee.current_bet = (self.player_quantity*5, 3)
        self.manager.players[self.manager.current_player].dices = [Dice()]
        self.assertTrue(self.referee.validate_calzo(self.manager.players, self.manager.current_player, self.manager.total_player_quantity))
