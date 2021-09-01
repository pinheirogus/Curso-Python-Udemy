
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as error:
        try:
            valor = float(valor)
            return valor
        except ValueError as error:
            pass


while True:

    numero = converte_numero(input('Digite um numero: '))
    if numero is None:
        print('Isso não é número.')
    else:
        print(numero * 5)
