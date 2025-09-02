
class ContadorPintas:
    def contar_pinta(self, dice_value, cachos, is_special_round):
        """
        Dada una pinta (As, tontos, trenes, etc...), cuenta todos los dados que contengan esa pinta
        y que estén contenidos en los cachos del juego, cuando no es ronda especial, los aces cuentan como comodines

        Returns:
            int: entero con cantidad de veces que se cuentan las pintas
        """
        counter = 0
        for cacho in cachos:
            cacho_dices = cacho.get_dices()
            for dice in cacho_dices:
                if dice.value == dice_value or (not is_special_round and dice.value == 1):
                    counter += 1


        return counter
