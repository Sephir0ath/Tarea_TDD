from .contador_pintas import ContadorPintas

class RoundReferee:
    def __init__(self):
        self.current_bet = None
        self.is_special_round = False
        self.counter = ContadorPintas()

    def handle_doubt(self, players, current_player, special_round_list, player_quantity):
        """
        Maneja la lógica cuando un jugador duda, primero determina qué jugador perdió,
        luego si es que la ronda actual era una ronda especial, resetea a las rondas normales,
        después quita un dado al perdedor y verifica si no hay que activar ronda especial o si hay que eliminar a un jugador.

        Returns:
            int: valor del jugador que empezará la siguiente ronda
        """
        if self.counter.contar_pinta(self.current_bet[1], players, self.is_special_round) >= self.current_bet[0]:
            loser_index = current_player  # El que dudó pierde
        else:
            loser_index = (current_player - 1) % len(players)  # El que apostó pierde

        if self.is_special_round:
            self.is_special_round = False

        players[loser_index].remove_dice()
        dice_count = len(players[loser_index].get_dices())

        if dice_count == 0:
            players.pop(loser_index)
            player_quantity -= 1
            next_player = loser_index % len(players)
            return next_player

        elif dice_count == 1 and not special_round_list[loser_index]:
            special_round_list[loser_index] = True
            self.is_special_round = True

        return loser_index


    def handle_calzo(self, players, current_player, special_round_list, player_quantity):
        """
        Maneja la lógica cuando un jugador calza, actúa similar a handle_doubt
        con la excepción de que sólo el jugador actual puede ganar o perder dados.

        Returns:
            int: valor del jugador que empezará la siguiente ronda
        """
        if self.counter.contar_pinta(self.current_bet[1], players, self.is_special_round) == self.current_bet[0]:
            players[current_player].add_dice() # el que calzó gana un dado
        else:
            players[current_player].remove_dice()

        if self.is_special_round:
            self.is_special_round = False

        dice_count = len(players[current_player].get_dices())
        if dice_count == 0:
            players.pop(current_player)
            player_quantity -= 1
            next_player = current_player % len(players)
            return next_player

        elif dice_count == 1 and not special_round_list[current_player]:
            special_round_list[current_player] = True
            self.is_special_round = True

        return current_player

    def validate_calzo(self, players, current_player, total_player_quantity):
        """
        Indica si el jugador puede calzar o no
        """
        if self.current_bet is None:
            return False

        return True
        dice_count = 0
        for player in players:
            dice_count += len(player.get_dices())

        if dice_count <= (total_player_quantity*5)/2 or len(players[current_player].get_dices()) == 1:
            return True

        return False

    def validate_doubt(self):
        if self.current_bet is None:
            return False

    def remove_player(self, players, player_index):
        """
        Remueve un jugador que ya no tiene dados
        """
        players.pop(player_index)
