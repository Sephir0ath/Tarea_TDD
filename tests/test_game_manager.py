import unittest
from idlelib.run import manage_socket
from unittest.mock import MagicMock

from src.game.game_manager import GameManager

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.player_quantity = 4
        self.manager = GameManager(self.player_quantity)


    def test_determinar_jugador_inicial(self):
        self.manager.set_initial_player()

        self.assertGreaterEqual(self.manager.initial_player, 0)
        self.assertLessEqual(self.manager.initial_player, self.manager.player_quantity)

