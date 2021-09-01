from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do saque precisa ser numérico.')
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.exibir_detalhes()