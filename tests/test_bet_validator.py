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

