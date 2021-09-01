import re


def limpa_cnpj(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    # cnpj = list(cnpj)
    return cnpj

def transforma_cnpj(cnpj):
    cnpj = [int(x) for x in cnpj]
    cnpj.pop()
    cnpj.pop()
    print(type(cnpj))
    print(cnpj)
    return cnpj


def calc_primeiro_digito(cnpj, vez=1):
    lista_calc = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    soma = 0
    if vez == 1:
        lista_calc.pop(0)
    elif vez == 2:
        pass
    else:
        print('Algo errado não está certo')
        return None

    for indice, numero in enumerate(lista_calc):
        soma += (cnpj[indice] * numero)
    digito = 11 - (soma % 11)

    if digito > 9:
        digito = 0

    cnpj.append(digito)
    return cnpj

#
# def calc_segundo_digito(cnpj):
#     lista_calc = [6,5,4,3,2,9,8,7,6,5,4,3,2]
#     soma = 0
#
#     for indice, numero in enumerate(lista_calc):
#         soma += (cnpj[indice] * numero)
#     digito = 11 - (soma % 11)
#
#     if digito > 9:
#         digito = 0
#
#     cnpj.append(digito)
#     return cnpj


while True:
    cnpj_original = input('Favor inserir o CNPJ com pontos, traços e dígitos: ')
    try:
        cnpj_limpo = transforma_cnpj(limpa_cnpj(cnpj_original))
        print('CNPJ depois de limpo: \n', cnpj_limpo)
        cnpj_atualizado = calc_primeiro_digito(cnpj_limpo)
        print('CNPJ após cálculo do primeiro dígito: \n', cnpj_atualizado)
        cnpj_atualizado = calc_primeiro_digito(cnpj_atualizado, 2)
        print('CNPJ após cálculo do segundo dígito: \n', str(cnpj_atualizado))
        print(''.join(map(str, cnpj_atualizado)))
        print('CNPJ original: \n', limpa_cnpj(cnpj_original))
        if ''.join(map(str, cnpj_atualizado)) == limpa_cnpj(cnpj_original):
            print(f'O CNPJ {cnpj_original} digitado é válido.')
        else:
            print(f'O CNPJ {cnpj_original} digitado é inválido.')
    except Exception as error:
        print(f'O CNPJ digitado é inválido, gerou exceção {error}')