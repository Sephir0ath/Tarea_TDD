from .dice import Dice

class Cacho:
    def __init__(self):
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

    def remove_dice(self):
        """
        Remueve un dado del cacho.
                    
        Returns:
            None
        """
        self.dices.pop()

    def add_dice(self):
        """Si es que no tiene 5 dados, añade uno

        Returns:
            None
        """
        if len(self.dices) < 5:
            self.dices.append(Dice())
