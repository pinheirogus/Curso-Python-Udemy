# num1 = input("Digite um número inteiro: ")
#
#
# try:
#
#     if num1.isnumeric() :
#         num1 = int(num1)
#         if (num1 % 2) == 0 :
#             print("Você digitou um número par.")
#         elif (num1 % 2) != 0:
#             print("Você digitou um número ímpar.")
#         else:
#             print("Você não digitou um número válido.")
#     else:
#         print("Você não digitou um número inteiro.")
# except:
#     print("Você não digitou um número.")

###################################################################################################################################

#hora_atual = input("Qual o horário atual? ")

###################################################################################################################################

nome = input("Por favor, digite seu primeiro nome: ")

try:
    if nome.isnumeric():
        print("Você não digitou um nome válido.")
    else:
        if len(nome) <= 4:
            print("Seu nome é curto.")
        elif (len(nome) == 5) or (len(nome) == 6):
            print("Seu nome é normal.")
        elif len(nome) > 6:
            print("Seu nome é muito grande.")
        else:
            print("Você não digitou um nome válido.1")
except:
    print("Você não digitou um nome válido.")

