from account import Account


class CurrentAccount(Account):
    def withdraw(self, value) -> float:
        balance_expected = self.balance - value
        if balance_expected < 0.0:
            raise ValueError(f'You do not have a balance to withdraw. Balance = {self.balance}')
        return balance_expected
