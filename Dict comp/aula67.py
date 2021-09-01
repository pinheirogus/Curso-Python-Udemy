
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ('chave3', 3),
]

# d1 = { x: y*2 for x, y in lista}
# d1 = { x.upper(): y.upper()*2 for x, y in lista}

d1 = { f'chave_{x}': x**2 for x in range(5)}


print(d1)