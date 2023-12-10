"""
# English
The relation between Car and Engine choose is Composition.

The relation between Manufacturer and Car choose is Aggregation.

# Portuguese
A relação entre Carro e Motor escolhida eh de Composicao.

A relação entre Fabricador e Carro escolhida eh de Agregacao.
"""


class Manufacturer:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_car_specification(self):
        for car in self.cars:
            print(f'Car: {car.name} | Engine: {car.engine.name}')


class Car:
    def __init__(self, name):
        self.engine = None
        self.name = name

    def insert_engine(self, name):
        self.engine = Engine(name)


class Engine:
    def __init__(self, name):
        self.name = name


volkswagen = Manufacturer('Volkswagen')
gol = Car('Gol')
gol.insert_engine('VHT')
volkswagen.add_car(gol)

volkswagen.show_car_specification()
