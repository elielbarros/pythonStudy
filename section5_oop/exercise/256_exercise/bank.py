from account import Account
from current_account import CurrentAccount
from customer import Customer


class Bank:
    def __init__(self):
        self.customers: list[Customer] | None = []
        self.accounts: list[Account] | None = []

    def insert_customer(self, customer: Customer):
        self.customers.append(customer)

    def insert_account(self, account: Account):
        self.accounts.append(account)

    def withdraw(self, customer: Customer, account: Account, value):
        self.__check_customer(customer)

        self.__check_account(account)

        self.__check_customer_account(customer, account)

        customer.account.withdraw(value)

    def __check_customer(self, customer: Customer):
        if customer not in self.customers:
            raise ValueError(f'Customer {customer.__dict__} is not from this bank')

    def __check_account(self, account: Account):
        if account not in self.accounts:
            raise ValueError(f'Account {account.__dict__} is not from this bank')

    def __check_customer_account(self, customer: Customer, account: Account):
        if account is not customer.account:
            raise ValueError(f'Account {account.account_number} is not from the customer "{customer.name}"')


b = Bank()
c1 = Customer('John', 16)
current_ac = CurrentAccount(123, 12345)
c1.insert_account(current_ac)

b.insert_customer(c1)
b.insert_account(current_ac)

b.withdraw(c1, current_ac, 5)  # output: You withdrew 5 from your account. Your actual balance is "-5"

current_ac2 = CurrentAccount(321, 654)
b.insert_account(current_ac2)
b.withdraw(c1, current_ac2, 5)

# customer_2 = Customer('Mary', 18)
# current_ac_2 = CurrentAccount(321, 54321)
# customer_2.insert_account(current_ac_2)
#
# b.withdraw(customer_2, current_ac_2, 5)
