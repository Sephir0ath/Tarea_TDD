from src.game.cacho import Cacho

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestCacho():
    def setUp(self):
        self.cacho = Cacho()
        self.cacho.roll_dices()

    def test_cacho_has_five_dices(self):
        assert len(self.cacho.get_dices()) == 5
