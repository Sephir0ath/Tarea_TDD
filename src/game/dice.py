from random import randint
from .enums import DiceNames

class Dice:
    def __init__(self):
        self.value = None
        self.value_name = None

    def roll(self):
        """Genera un valor, lo almacena y guarda el nombre respectivo del valor, también almacena el nombre de la pinta

        Returns:
            int: valor generado por el dado
        """
        generated_value = randint(1, 6)
        self.value = generated_value
        self.value_name = DiceNames[f"DICE{generated_value}"].value

        return generated_value

