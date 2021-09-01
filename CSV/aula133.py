
import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    #
    # #next(dados)
    # for dado in dados:
    #     print(dado)

    # dados = csv.DictReader(arquivo)
    #
    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])
    #

    dados = [x for x in csv.DictReader(arquivo)]

with open('clientes2.csv', 'w') as arquivo:
    #Sozinha esta função não escreve nada no arquivo
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar = '"',
        quoting = csv.QUOTE_ALL
    )

    print(dados)

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )

