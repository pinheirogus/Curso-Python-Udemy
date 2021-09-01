
from itertools import count

contador = count(start=5, step=2)

print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))


for valor in contador:
    print(valor)

    if valor >= 10:
        break






