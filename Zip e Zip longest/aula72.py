


cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']



estados = ['SP', 'MG', 'BA']

#zip só une até terminar a menor lista
cidades_estados = zip(cidades, estados)


print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))

################################################################################################################################################################################################

from itertools import zip_longest, count

cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')

print(list(cidades_estados))

indice = count()

cidades_estados = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)