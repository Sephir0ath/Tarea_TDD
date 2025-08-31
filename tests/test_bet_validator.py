import unittest

from src.game.bet_validator import BetValidator
from src.game.round_referee import RoundReferee

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestBetValidator(unittest.TestCase):
    def setUp(self):
        self.round_referee = RoundReferee()
        self.bet_validator = BetValidator()

    def test_validar_apuesta_inicial(self):
        self.assertIsNone(self.bet_validator.current_bet)

        first_bet = (2, 2)
        is_bet_valid = self.bet_validator.check_bet(first_bet, False)
        self.assertTrue(is_bet_valid)

    def test_validar_apuesta_mayor(self):
        self.bet_validator.current_bet = (1,5)
        self.assertTrue(self.bet_validator.check_bet((3, 5), False))
        self.assertTrue(self.bet_validator.current_bet, (3,5))

    def test_validar_apuesta_menor(self):
        self.bet_validator.current_bet = (3,2)
        new_bet = (2, 2)
        is_bet_valid = self.bet_validator.check_bet(new_bet, False)
        self.assertFalse(is_bet_valid)
    
    def test_validar_apuesta_inicial_con_ases(self):
        self.round_referee.current_bet = None
        self.bet_validator = BetValidator()

        # Comprobar que si una apuesta inicial es de aces y es una ronda normal entonces no es valida
        first_bet = (2, 1)
        is_bet_valid = self.bet_validator.check_bet(first_bet, False)
        self.assertFalse(is_bet_valid)