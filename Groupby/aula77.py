from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joanma', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]
ordena = lambda item: item['nota']

# É imprescindível que os valores estejam ordenados!

alunos.sort(key=ordena)

# for aluno in alunos:
#     print(aluno)

alunos_agrupados = groupby(alunos, ordena)

for grupo, valores_agrupados in alunos_agrupados:
    print(f'Grupo: {grupo}')

    qtde_alunos = len(list(valores_agrupados))

    print(f'{qtde_alunos} alunos tiraram a nota {grupo}')

    # for aluno in valores_agrupados:
    #     print(aluno)
    #
    # print()