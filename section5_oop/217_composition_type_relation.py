"""
# English
Class Relation - Composition - Strong Coupling - Composition is a specialization of Aggregation

With Composition when we delete principal class then related class will be deleted too.

# Portuguese
Class Relation - Composition - Strong Coupling - Composition eh a especializacao de Aggregation

Com Composition quando nos deletamos a classe principal entao a classe relacionada serah deletada junto
"""


class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, street, number):
        self.addresses.append(Address(street, number))

    def add_external_address(self, address):
        self.addresses.append(address)

    def list_addresses(self):
        print(f'{self.name} addresses:')
        for address in self.addresses:
            print(f'Street: "{address.street}" | Number: {address.number}')

    def __del__(self):
        print(f'DELETING INSTANCE Client: {self.name}')


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print(f'DELETING INSTANCE Address: {self.street}, {self.number}')


client = Client('John')
client.add_address('Road Mary Roe', 123)
client.add_address('Road William Wilson', 456)
client.list_addresses()
print('GARBAGE COLLECTOR FROM HERE')
# output:
# GARBAGE COLLECTOR FROM HERE
# DELETING INSTANCE Client: John
# DELETING INSTANCE Address: Road William Wilson, 456
# DELETING INSTANCE Address: Road Mary Roe, 123

c1 = Client('Anna')
c1.add_address('Road Emily Johnson', 789)
c1.add_address('Road Susan Anderson', 101112)

# If we add an external class to Client, then this address will not be deleted as c1
address_ex = Address('Road Jessica Miller', 131415)
c1.add_external_address(address_ex)
client.list_addresses()
# If we delete client here, Garbage Collector will not delete our Client 1 because we already did it.
del c1
# output:
# DELETING INSTANCE Address: Road Susan Anderson, 101112
# DELETING INSTANCE Address: Road Emily Johnson, 789

print('GARBAGE COLLECTOR FROM HERE')
