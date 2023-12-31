from account import Account


class CurrentAccount(Account):
    def withdraw(self, value) -> float:
        balance_expected = self.balance - value
        if balance_expected < -100.0:
            raise ValueError(f'The {value} cant be taken. Your balance is {self.balance}.')
        return balance_expected

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'({self.agency!r}, {self.account_number!r}, {self.balance!r})'
        return f'{class_name}{attributes}'

