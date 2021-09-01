from dados import lista, produtos, pessoas

# nova_lista = filter(lambda x: x>5, lista)
# print(list(nova_lista))

# nova_lista = [x for x in lista if x >5]
# print(list(nova_lista))


########################################################################################################################

# nova_lista = filter(lambda p: p['preco'] > 20, produtos)
#
# for produto in nova_lista:
#     print(produto)
#
########################################################################################################################
#
# def filtra(produto):
#     if produto['preco'] > 50:
#         return True
#     else:
#         return False
#
# nova_lista = filter(filtra, produtos)
#
# for produto in nova_lista:
#     print(produto)

########################################################################################################################

# def filtra(pessoa):
#     if pessoa['idade'] < 18:
#         return True
#
#
# nova_lista = filter(filtra, pessoas)
#
# for pessoa in nova_lista:
#     print(pessoa)