
from vendas.formata import preco


def aumento(valor, porcentagem, formatacao = False):
    r = valor + (valor * (porcentagem / 100))

    if formatacao:
        return preco.real(r)
    return r

def reducao(valor, porcentagem, formatacao = False):
    r = valor - (valor * (porcentagem / 100))

    if formatacao:
        return preco.real(r)
    return r

