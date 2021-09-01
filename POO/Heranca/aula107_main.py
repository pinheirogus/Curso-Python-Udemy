
from aula107_classes import Pessoa, Cliente, Aluno, ClienteVIP

c1 = Cliente('Luiz', 45)

print(c1.nome)

a1 = Aluno('Maria', 65)

print(a1.nome)

a1.falar()
c1.falar()
c1.comprar()
a1.estudar()

vip1 = ClienteVIP('Marcos', 32, 'Miranda')

vip1.falar()