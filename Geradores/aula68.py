
# lista = [0,1,2,3,4,5]

# Transforma a lista em um iterador
# lista = iter(lista)

# print(next(lista))

# print(hasattr(lista, '__next__'))

# print(next(lista))
# print(next(lista))

########################################################################################################################

import sys

# lista = list(range(10))

# print(sys.getsizeof(lista))

#######################################################################################################################

#Criando uma função geradora, que entrega o próximo valor a cada chamada

import time
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)

# g = gera()


# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#######################################################################################################################

l1 = [x for x in range(1000)]

# Utilizando os parenteses você cria um gerador

l2 = (x for x in range(1000))

print(type(l1))
print(sys.getsizeof(l1))

print(type(l2))
print(sys.getsizeof(l2))

