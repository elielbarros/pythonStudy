from account import Account
from current_account import CurrentAccount
from customer import Customer


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def insert_customer(self, customer: Customer):
        self.customers.append(customer)

    def insert_account(self, account: Account):
        self.accounts.append(account)

    def withdraw(self, customer: Customer, account: Account, value):
        if customer not in self.customers:
            raise ValueError(f'Customer {customer.__dict__} is not from this bank')

        if account not in self.accounts:
            raise ValueError(f'Account {account.__dict__} is not from this bank')

        customer.account.withdraw(value)


b = Bank()
customer = Customer('John', 16)
current_ac = CurrentAccount(123, 12345)
customer.insert_account(current_ac)

b.insert_customer(customer)
b.insert_account(current_ac)

b.withdraw(customer, current_ac, 5) # output: You withdrew 5 from your account. Your actual balance is "-5"

# customer_2 = Customer('Mary', 18)
# current_ac_2 = CurrentAccount(321, 54321)
# customer_2.insert_account(current_ac_2)
#
# b.withdraw(customer_2, current_ac_2, 5)
