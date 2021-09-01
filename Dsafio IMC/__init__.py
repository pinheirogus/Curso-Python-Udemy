nome = 'Gustavo'
idade = 30
altura = 1.8
peso = 85.2
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e {altura} de altura. Nasceu no ano de {nascimento}. Seu IMC é {imc:.2f}.')
print("{0} tem {1} anos e {2} de altura. Com base nisso, seu IMC é {3:.2f}.".format(nome, idade, altura, imc))
