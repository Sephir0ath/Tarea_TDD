import unittest

from src.game.enums import DiceNames
from src.game.dice import Dice

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestDice(unittest.TestCase):
    def test_create_dice_with_value(self):
        dice = Dice()
        dice.roll()
        assert 1 <= dice.value <= 6

    def test_guardar_nombre_del_dado(self):
        valid_names = []
        for x in DiceNames:
            valid_names.append(x.value)

        dice = Dice()
        dice.roll()

        assert dice.value_name in valid_names