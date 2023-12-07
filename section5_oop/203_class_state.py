"""
# English
Class attributes maintain a state.

When we create an instance from class and fill the attributes that belong to this class, these attributes will store
a state.

This information will be maintained until this information is not changed by us.

# Portuguese
Os atributos da classe mantem um estado.

Quando fazemos a instancia da classe e preenchemos os atributos que pertencem a classe, esses atributos armazenam um
estado de informacao.

Essa informacao sera mantida ateh a informacao seja alterada por nos
"""


class Cam:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        print(f'{self.name} is filming...')
        self.filming = True


cam1 = Cam('Cannon')
cam1.film()  # output: Cannon is filming...
# Actually, the attribute 'filming' from class Cam is True, because we ask Cam to film, and it will stay as True
# until we let it True
print(cam1.filming)  # output: True

cam2 = Cam('Sony')
# Since we did not ask for cam2 to 'film', so the attribute state will stay as False, defined on __init__ method.
print(cam2.filming)  # output: False
