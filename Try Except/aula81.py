
#Este tipo de tratamento de exceção não é boa prática
#
# try:
#     print(a)
# except:
#     print("Erro")

########################################################################################################################

#Tratamento adequado:

try:
    print(a)
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro: ', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado...')
else:
    print('Seu código no bloco try foi executado com sucesso')
finally:
    print('Este código sempre será executado, independente de ocorrer erro ou não.')

