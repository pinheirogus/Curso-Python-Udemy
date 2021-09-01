"""
Combinations, Permutations e Product - Itertools
Combinação - Não cria conjuntos com os mesmos elementos em ordem diferente.
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos

"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']


# for grupo in combinations(pessoas, 2):
#     print(grupo)
# for grupo in permutations(pessoas, 2):
#     print(grupo)
# for grupo in product(pessoas, repeat=2):
#     print(grupo)