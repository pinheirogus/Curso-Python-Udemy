
# lists, tuples, str são sequencias e portanto são iteráveis

nome = 'Luiz Otávio'

iterador = iter(nome)

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')

for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')

#Este segundo for não resulta em nada pois o gerador já exauriu seus valores.
#O for transforma o objeto iterável passado para um iterador
#Porém o for não apresenta erro de StopIteration
for letra in gerador:
    print(letra)

    