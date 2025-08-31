
class ContadorPintas:
    def contar_pinta(self, dice_value, cachos, is_special_round=True):
        counter = 0
        for cacho in cachos:
            cacho_dices = cacho.get_dices()
            for dice in cacho_dices:
                if dice.value == dice_value or (not is_special_round and dice.value == 1):
                    counter += 1


        return counter
