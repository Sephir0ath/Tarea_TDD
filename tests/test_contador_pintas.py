import unittest

from src.game.contador_pintas import ContadorPintas
from src.game.cacho import Cacho
from src.game.enums import DiceNames
from unittest.mock import MagicMock

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestContadorPintas(unittest.TestCase):
    def setUp(self):
        self.contador_pintas = ContadorPintas()
        self.cachos_list = []

        for i in range(4):  # Crear 4 jugadores (cachos)
            self.cachos_list.append(Cacho())
            self.cachos_list[i].roll_dices()

    def test_contar_apariciones_pinta(self):
        for i in self.cachos_list:
            for x in range(5):
                if x == 0:
                    i.get_dices()[x].value = 2
                else:
                    i.get_dices()[x].value = 3


        tontos_quantity = self.contador_pintas.contar_pinta(2, self.cachos_list)
        self.assertEqual(tontos_quantity, 4)

    def test_contar_aces_como_comodines(self):
        for i in range(4):
            self.cachos_list[i].roll_dices()

        for i in self.cachos_list:
            for x in range(5):
                if x == 0:
                    i.get_dices()[x].value =2
                else:
                    i.get_dices()[x].value = 3

            self.cachos_list[3].get_dices()[4].value = 1

        tontos_quantity = self.contador_pintas.contar_pinta(2, self.cachos_list, False)
        assert tontos_quantity == 5
    