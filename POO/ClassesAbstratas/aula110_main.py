from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
#
# class B(A):
#     def falar(self):
#         print('Falando em B.')
#
#
# b = B()
#
# b.falar()

from classes.contaPoupanca import ContaPoupanca
from classes.contaCorrente import ContaCorrente

poupancaBB = ContaPoupanca(1111, 2222, 0)

poupancaBB.depositar(10)
poupancaBB.sacar(5)
poupancaBB.sacar(5)
poupancaBB.sacar(5)

print('##############################################################################')

correnteBB = ContaCorrente(1111, 3333, 0, 500)

correnteBB.depositar(100)
correnteBB.sacar(500)
correnteBB.sacar(101)