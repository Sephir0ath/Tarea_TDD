import unittest

from src.game.bet_validator import BetValidator
from src.game.dice import Dice
from src.game.game_manager import GameManager
from src.game.round_referee import RoundReferee


class TestIntegracion(unittest.TestCase):
    def setUp(self):
        self.player_quantity = 2 # Seteamos a 2 jugadores, Jugador A y B
        self.game_manager = GameManager(self.player_quantity)
        self.arbitro = RoundReferee()
        self.bet_validator = BetValidator()

    def test_integracion(self):
        # Ronda 1, haremos que current_player pierda un dado haciendo una apuesta imposible
        self.game_manager.roll_dices()

        self.game_manager.current_player = 0 # Jugador A
        player_bet = (15, 6) # Como solo hay 10 dados en juego, esta apuesta jamás se podrá cumplir
        if self.bet_validator.check_bet(player_bet, False): # Si la nueva apuesta es válida (cumple las condiciones necesarias), cambia la apuesta actual
            self.arbitro.current_bet = player_bet

        current_player = self.game_manager.next_turn() # Pasamos al siguiente jugador (jugador B)
        current_player = self.arbitro.handle_doubt(self.game_manager.players,
                                                   current_player,
                                                   self.game_manager.has_activated_special_round,
                                                   self.player_quantity) # Pasamos a jugador A

        self.game_manager.current_player = current_player # Nos aseguramos que se guarde correctamente el jugador

        self.assertEqual(len(self.game_manager.players[current_player].get_dices()), 4) # Chequeamos que el jugador que hizo la primera apuesta (jugador A) perdió un dado
        self.bet_validator.current_bet = None

        # Ronda 2, vamos a hacer una apuesta inicial y otro jugador va a tratar de calzar (no puede porque no es ronda especial)
        # Luego, verificaremos que se cambie la apuesta actual

        self.game_manager.roll_dices()

        player_bet = (4, 3)
        if self.bet_validator.check_bet(player_bet, False):
            self.arbitro.current_bet = player_bet

        current_player = self.game_manager.next_turn() # jugador B
        self.assertFalse(self.arbitro.validate_calzo(self.game_manager.players,
                                                     current_player,
                                                     self.player_quantity))

        player_bet = (20, 3)
        if self.assertTrue(self.bet_validator.check_bet(player_bet, False)):
            self.arbitro.current_bet = player_bet

        current_player = self.game_manager.next_turn() # jugador A

        # Ahora vamos a hacer que el jugador B pierda un dado
        current_player = self.arbitro.handle_doubt(self.game_manager.players,
                                                   current_player,
                                                   self.game_manager.has_activated_special_round,
                                                   self.player_quantity)

        self.game_manager.current_player = current_player
        self.bet_validator.current_bet = None

        # Ronda 3, para hacer más rápido el procedimiento, se va a cambiar la cantidad de dados del jugador A a 2 para forzar ronda especial
        self.game_manager.roll_dices()

        current_player = self.game_manager.next_turn() # Jugador A
        self.game_manager.players[current_player].dices = [Dice(), Dice()]

        player_bet = (20, 3) # Nuevamente haremos una apuesta imposible para que el jugador A pierda un dado
        if self.bet_validator.check_bet(player_bet,
                                        False):  # Si la nueva apuesta es válida (cumple las condiciones necesarias), cambia la apuesta actual
            self.arbitro.current_bet = player_bet

        current_player = self.game_manager.next_turn()  # jugador B
        current_player = self.arbitro.handle_doubt(self.game_manager.players, current_player,
                                                   self.game_manager.has_activated_special_round,
                                                   self.player_quantity)  # Pasamos a jugador A
        self.game_manager.current_player = current_player
        self.assertTrue(len(self.game_manager.players[current_player].get_dices()), 1) # El jugador A tiene solo un dado
        self.bet_validator.current_bet = None

        # Ahora se activa ronda especial, primero probaremos que se puede iniciar con ases la apuesta
        player_bet = (1, 1)
        self.assertTrue(self.bet_validator.check_bet(player_bet, True))
        self.arbitro.current_bet = player_bet

        player_bet = (2, 3)
        current_player = self.game_manager.next_turn() # Jugador B
        self.assertTrue(self.bet_validator.check_bet(player_bet, True))
        self.assertFalse(self.bet_validator.check_bet(player_bet, False)) # Esto es para probar que en una ronda no especial no se podría usar esa apuesta
        self.arbitro.current_bet = player_bet

