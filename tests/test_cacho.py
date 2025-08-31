import unittest

from src.game.cacho import Cacho

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestCacho(unittest.TestCase):
    def setUp(self):
        self.cacho = Cacho()

    def test_cacho_has_five_dices(self):
        self.assertEqual(len(self.cacho.get_dices()), 5)
