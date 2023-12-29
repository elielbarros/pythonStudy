from account import Account


class CurrentAccount(Account):
    def withdraw(self, value) -> float:
        balance_expected = self.balance - value
        if balance_expected < -100.0:
            raise ValueError(f'The {value} cant be taken. Your balance is {self.balance}.')
        return balance_expected
