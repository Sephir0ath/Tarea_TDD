from random import randint

class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        """Genera un valor, lo almacena y guarda el nombre respectivo del valor

        Returns:
            int: valor generado por el dado
        """
        generated_value = randint(1, 6)
        self.value = generated_value

        return generated_value