# """
# -> É uma lista de listas de números inteiros
# -> As listas internas tem o tamanho de 10 elementos
# -> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
# Exercício
# -> Crie uma função que encontra o primeiro duplicado considerando o segundo
#     número como a duplicação. Retorne a duplicação considerada.
#         Requisitos:
#             A ordem do número duplicado é considerada a partir da segunda
#             ocorrência do número, ou seja, o número duplicado em si.
#             Exemplo:
#                 [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#                 [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#             Se não encontrar duplicados na lista, retorne -1
# """


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def retornarDuplicado(listaDeNumeros):
    lista_de_retornos = list()
    for i in listaDeNumeros:
        l1 = set(i)
        l1 = sorted(list(l1))
        if l1 == sorted(i):
            lista_de_retornos.append(-1)
        else:
            for n, value in enumerate(i):
                l1 = set(i[:n+1])
                l1 = list(l1)
                l1.sort()
                l2 = sorted(i[:n+1])
                if l1 == l2:
                    pass
                else:
                    lista_de_retornos.append(value)
                    break          
    return lista_de_retornos

print(retornarDuplicado(lista_de_listas_de_inteiros))
