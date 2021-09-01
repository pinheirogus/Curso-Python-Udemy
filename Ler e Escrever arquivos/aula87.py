# Primeiro modo
#
# file = open('abc.txt', 'w+')
#
# file.write('Linha 1 \n')
# file.write('Linha 2 \n')
# file.write('Linha 3 \n')
#
# file.seek(0,0)
# print('Lendo linhas: ')
# print(file.read())
# print('#################################################')
#
# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('#################################################')
#
# file.seek(0,0)
# print(file.readlines())
# print('#################################################')
#
# file.seek(0,0)
# for linha in file.readlines():
#     print(linha, end='')
#
#
# file.close()

# Segundo modo

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()



# Terceiro e melhor modo para o Python

# r é o moodo read, leitura
# w é o modo write, apaga o arquivo todo e escreve por cima
# a é o modo append, adicionar conteúdo sem remover
# + é um tipo de modo de expansão, pra poder fazer..tudo?

# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())
