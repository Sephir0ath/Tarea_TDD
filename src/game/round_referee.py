from .contador_pintas import ContadorPintas

class RoundReferee:
    def __init__(self):
        self.current_bet = ()
        self.is_special_round = False
        self.counter = ContadorPintas()

    def handle_doubt(self, players, current_player):
        if self.counter.contar_pinta(self.current_bet[1], players, self.is_special_round) >= self.current_bet[0]:
            players[current_player].remove_dice()
        else:
            last_player = (current_player-1) % len(players)
            players[last_player].remove_dice()