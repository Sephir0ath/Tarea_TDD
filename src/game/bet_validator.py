class BetValidator:
    def __init__(self):
        self.current_bet = None

    def check_bet(self, new_bet, is_special_round):
        if self.current_bet is None:
            if not is_special_round:
                self.current_bet = new_bet
                return True
            else:
                return False

        if new_bet[0] > self.current_bet[0]:
            self.current_bet = new_bet
            return True

        return False