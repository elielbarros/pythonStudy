"""
# English
- secrets.SystemRandom() -
class provided in the secrets module in Python that uses the operating system's random number generator to generate
cryptographically secure pseudorandom numbers. The idea behind SystemRandom is to use operating system entropy
sources, making the generated numbers more secure for cryptographic purposes.

This class is a subclass of random.SystemRandom, which in turn is a subclass of random.Random. This means you can use
it in a similar way to other random number generation classes, but with the added advantage of using operating system
fonts to increase the quality of the randomness.

seed does not work with secrets.SystemRandom()

# Portuguese
- secrets.SystemRandom() -

classe fornecida no módulo secrets em Python que utiliza o gerador de números aleatórios do sistema operacional para
gerar números pseudoaleatórios criptograficamente seguros. A ideia por trás do SystemRandom é usar fontes de entropia
do sistema operacional, tornando os números gerados mais seguros para propósitos criptográficos.

Esta classe é uma subclasse de random.SystemRandom, que, por sua vez, é uma subclasse de random.Random. Isso
significa que você pode usá-la de maneira semelhante a outras classes de geração de números aleatórios,
mas com a vantagem adicional de usar fontes do sistema operacional para aumentar a qualidade da aleatoriedade.

seed nao funciona com secrets.SystemRandom()
"""
import secrets
import string as s
from secrets import SystemRandom as Sr

print(s.ascii_letters, s.digits, s.punctuation)
random_things = s.ascii_letters + s.digits + s.punctuation
password = ''.join(Sr().choices(random_things, k=15))
print(password)


random = secrets.SystemRandom()

names = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(names)
print(names)

new_names = random.sample(names, k=2)
print(new_names)

new_names = random.choices(names, k=2)
print(new_names)

name = random.choice(names)
print(name)

