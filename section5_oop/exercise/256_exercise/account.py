from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def withdraw(self, value) -> float:
        raise NotImplementedError('Implement log method')

    def deposit(self, value):
        self.balance += value
