import unittest

from src.game.cacho import Cacho
from src.game.dice import Dice

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestCacho(unittest.TestCase):
    def setUp(self):
        self.cacho = Cacho()
        self.cacho.roll_dices()

    def test_cacho_has_five_dices(self):
        self.assertEqual(len(self.cacho.get_dices()), 5)

    def test_cacho_can_roll_values(self):
        self.cacho.roll_dices()

        new_values = []
        for dice in self.cacho.get_dices():
            new_values.append(dice.value)

        for dice_value in new_values:
            assert 1 <= dice_value <= 6

    def test_cacho_removes_and_adds_dice(self):
        self.cacho.dices = [Dice()]
        self.cacho.remove_dice()
        assert len(self.cacho.dices) == 0

        self.cacho.add_dice()
        assert len(self.cacho.dices) == 1