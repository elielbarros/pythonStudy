"""
# English
Class Relation - Aggregation - Moderate Coupling - Aggregation is a type of Association

When a class need another class to work perfectly, these classes has an Aggregation Relation. But one class could be
created independently of another class.

Generally this Relation Type is a relation of One class to Many Classes.

For example:    One car could be created without a wheel and 'vice versa'. But the Car will not work well without the
                wheel. So the car has an Aggregation with Wheel.

Could exist controversy about Aggregation definition.

# Portuguese
Class Relation - Aggregation - Acoplamento Moderado - Aggregation eh um tipo de Association

Quando uma classe precisa de outra classe para funcionar perfeitamente. Essas classes tem uma relacao de Agregacao. Mas
uma classe pode ser criada independente da outra classe.

Geralmente esse tipo de Relacao eh uma relacao de uma classe para varias classes.

Por Exemplo:    Um caro pode ser criado sem a roda e vice versa. Mas um carro precisa da roda para funcionar
                perfeitamente. Entao o carro tem uma relacao de Aggregation com a roda.

Pode existir controversias sobre a definicao de Aggregation
"""


class ShoppingCart:
    def __init__(self, name):
        self.name = name
        self._product = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def insert_product(self, product):
        self._product.append(product)

    def total(self):
        print(sum([product.price for product in self._product]))

    def list_shopping_cart(self):
        print(f'{self.name} products:')
        for item in self._product:
            print(f'{item.name} = {item.price}')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


sandwich = Product('Sandwich', 2.5)
pen = Product('Pe', 1.0)
shopping_cart = ShoppingCart('John')
shopping_cart.insert_product(sandwich)
shopping_cart.insert_product(pen)
shopping_cart.list_shopping_cart()
shopping_cart.total()
