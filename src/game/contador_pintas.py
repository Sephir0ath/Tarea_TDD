class ContadorPintas:
    def contar_pinta(self, dice_value, cachos):
        counter = 0
        for cacho in cachos:
            cacho_dices = cacho.get_dices()
            for dice in cacho_dices:
                if dice.value == dice_value:
                    counter += 1
                print(dice.value)

        return counter
