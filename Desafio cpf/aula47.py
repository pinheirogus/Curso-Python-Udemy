novo_cpf = input("Favor digite seu CPf sem pontos: ")

#Objetivo: checar se cpf_calculado é igual a novo_cpf e dizer se é válido


novo_cpf = list(novo_cpf)

for i,n in enumerate(novo_cpf):
    novo_cpf[i] = int(novo_cpf[i])



cpf_orig = list(novo_cpf)


novo_cpf[9] = 0
novo_cpf[10] = 0

print("CPF digitado sem os últimos dois dígitos: ", novo_cpf)
print("CPF original antes das verificações: ", cpf_orig)

#Verificação do primeiro dígito

d = 0
sum1 = int()
verif1 = int()

for i in range(10, 1, -1):
    # print(i)
    sum1 += novo_cpf[d] * i
    # print(sum1)
    d+= 1

    
verif1 = 11 - ( sum1 % 11)
print("Primeiro dígito verificador ", verif1)
if verif1 > 9:
    novo_cpf[9] = 0
else:
    novo_cpf[9] = verif1

print("Novo cpf após primeiro dígito verificador ", novo_cpf)


#Verificação do segundo dígito

d = 0
sum2=int()
verif2 = int()

for i in range(11, 1, -1):
    # print(i)
    sum2 += novo_cpf[d] * i
    # print(sum2)
    d+= 1

    
verif2 = 11 - ( sum2 % 11)
print("Segundo dígito verificador ", verif2)
if verif2 > 9:
    novo_cpf[10] = 0
else:
    novo_cpf[10] = verif2

print("Novo cpf após segundo dígito verificador ", novo_cpf)

print("CPF original: ", cpf_orig)

if novo_cpf == cpf_orig:
    print("O CPF digitado é válido.")
else:
    print("O CPF digitado é inválido.")