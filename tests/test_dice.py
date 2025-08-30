import unittest

from src.game.dice import Dice

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestDice(unittest.TestCase):
    def test_create_dice_with_value(self):
        dice = Dice()
        dice.roll()
        assert 1 <= dice.value <= 6
