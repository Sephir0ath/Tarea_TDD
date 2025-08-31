from .dice import Dice

class Cacho:
    def __init__(self):
        self.dices = []
        for i in range(5):
            self.dices.append(Dice())

    def get_dices(self):
        """
        Returns:
            a list of dice objects
        """
        return self.dices


