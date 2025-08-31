class BetValidator:
    def __init__(self):
        self.current_bet = None

    def check_bet(self, new_bet):
        if self.current_bet is None:
            self.current_bet = new_bet
            return True
        else:
            return False

        return False