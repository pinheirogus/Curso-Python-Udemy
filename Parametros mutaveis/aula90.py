#Este é o problema, ele pode acontecer com listas e dicionários como args mutáveis em funções.
#Variáveis imutáveis como tuplas, strings, números, booleanos não têm esse problema.

# def lista_de_clientes(clientes_iteravel, lista=[]):
#     lista.extend(clientes_iteravel)
#     return lista
#
# clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
#
# clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
#
# print(clientes1)
# print(clientes2)

#######################################################################################################################

#Para resolver o problema:

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], ['Bruno'])

clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)
