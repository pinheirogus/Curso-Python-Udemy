################################
# STACKS
#
# livros = list()
#
# livros.append('Livro 1')
# livros.append('Livro 2')
# livros.append('Livro 3')
# livros.append('Livro 4')
# livros.append('Livro 5')
#
# print(livros)
#
# livro_removido = livros.pop()
#
# print(livros, livro_removido)

################################
################################
# QUEUES

from collections import deque

# fila = deque(maxlen = 4)
#
# fila.append('Joãozinho')
#
# fila.append('Maria')
# fila.append('Luiz Otávio')
# fila.append('Marcos')
# fila.append('José')
#
# for nome in fila:
#     print(nome)
#
# fila.popleft()


from time import sleep

fila = deque(maxlen = 10)
#
# for i in range(1000):
#     fila.append(i)
#     print(fila)
#     sleep(1)

fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])

fila.extend('Luiz')
fila.remove(9)

# print(fila.index('L', 0, 3))

print(fila)

fila.reverse()
print(fila)

fila.rotate(2)
print(fila)