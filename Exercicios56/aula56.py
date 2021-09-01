def funcao1(f2, *args):
    return f2(*args)

def funcao2(num1):
    return 1+num1

def funcao3(nome, saudacao):
    return f'{saudacao}, {nome}'

execucao = funcao1(funcao3, 'Gustavo', 'Olá')

print(execucao)

    