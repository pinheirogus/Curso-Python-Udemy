# import re


string = '01234567890123456789012345678901234567890123456789'

n = '9'

lista = [elem+n for elem in string.split(n) if elem]

# lista = [elemen for elemen in re.split('(9)', string)]

retorno = '.'.join(lista)

print(lista)


print(retorno)