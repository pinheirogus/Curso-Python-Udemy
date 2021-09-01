
from aula106_classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)

cliente1.inserir_endereco('Belo Horizonte', 'MG')

cliente1.listar_enderecos()
print()
del cliente1
print()

cliente2 = Cliente('Maria', 55)

cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')

cliente2.listar_enderecos()

cliente3 = Cliente('João', 19)
cliente3.inserir_endereco('São Paulo', 'SP')

cliente3.listar_enderecos()

print('#################################################################################################')