import random
import string

# inteiro = random.randint(10, 20)
# inteiro = random.randrange(3, 74, 1)

# flutuante = random.uniform(10, 20)
# flutuante = random.random()
#
# print(inteiro)
# print(flutuante)
#
# lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
#
# sorteio = random.choice(lista)

# Esta função escolhe aleatoriamente um grupo de k itens do objeto passado COM possibilidade de repetição
# sorteio = random.choices(lista, k=2)

# Esta função escolhe aleatoriamente um grupo de k itens do objeto passado SEM possibilidade de repetição
# sorteio = random.sample(lista, 2)

#Embaralha a lista
# random.shuffle(lista)

# print(sorteio)

#Gera senha aleatória com componentes escolhidos ao acaso

# letras = string.ascii_letters
# digitos = string.digits
# caracteres = '!@#$%&*()_.-'
#
# geral = letras + digitos + caracteres
#
# senha = "".join(random.choices(geral, k=20))
#
# print(senha)
# print(letras)
# print(digitos)
# print(caracteres)
# print(geral)

# Gera senha aleatória com pelo menos um de cada componente

letras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
digitos = string.digits
caracteres = '!@#$%*.,_'
geral = letras_minusculas + letras_maiusculas + digitos + caracteres

senha = random.choice(letras_minusculas) + random.choice(letras_maiusculas) + random.choice(digitos) + random.choice(caracteres) + "".join(random.choices(geral, k=4))

print(senha)