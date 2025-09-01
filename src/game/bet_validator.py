class BetValidator:
    def __init__(self):
        self.current_bet = None

    def check_bet(self, new_bet, is_special_round):
        if self.current_bet is None:
            if not is_special_round and not new_bet[1] == 1:
                self.current_bet = new_bet
                return True
            if is_special_round and new_bet[1] == 1:
                self.current_bet = new_bet
                return True
            else:
                return False

        if self.current_bet[1] == 1 and new_bet[1] != 1 and not is_special_round:
            min_required = self.current_bet[0] * 2 + 1
            if new_bet[0] >= min_required:
                self.current_bet = new_bet
                return True
            else:
                return False

        elif new_bet[0] > self.current_bet[0]:
            self.current_bet = new_bet
            return True

        elif new_bet[0] == self.current_bet[0] and new_bet[1] > self.current_bet[1]:
            self.current_bet = new_bet
            return True

        elif self.current_bet[0] % 2 == 0 and new_bet[0] == self.current_bet[0]//2 and new_bet[1] == 1 and not is_special_round:
            self.current_bet = new_bet
            return True
        elif self.current_bet[0] % 2 == 1 and new_bet[0] == (self.current_bet[0]//2)+1 and new_bet[1] == 1 and not is_special_round:
            self.current_bet = new_bet
            return True

        return False