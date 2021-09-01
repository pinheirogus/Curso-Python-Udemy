# Generalizando para não repetir o código!


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando.')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        print(f'{self.nome}, {self.idade} anos, criado com sucesso.')
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        # Como a classe Cliente não possui o método falar(), o Python busca na superclasse o método.
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')