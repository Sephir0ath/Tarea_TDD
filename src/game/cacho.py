from .dice import Dice

class Cacho:
    def __init__(self, id=None):
        self.id = id
        self.dices = []
        for i in range(5):
            self.dices.append(Dice())

    def get_dices(self):
        """
        Returns:
            una lista de objetos dado
        """
        return self.dices

    def roll_dices(self):
        """
        Lanza todos los dados que están dentro del cacho

        Returns:
            None
        """
        for dice in self.dices:
            dice.roll()


