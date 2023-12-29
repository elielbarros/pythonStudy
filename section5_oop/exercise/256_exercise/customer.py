from person import Person
from account import Account


class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None

    def insert_account(self, account: Account):
        self.account = account
