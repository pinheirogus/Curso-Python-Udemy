
from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.id = self.gera_id()

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer enquanto fala.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come.')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def calcular_ano_nasc(self):
        return self.ano_atual - self.idade

    # cria uma instância da classe a partir dos argumentos passados
    # @classmethod
    # def por_ano_nasc(cls, nome, ano_nascimento):
    #     idade = cls.ano_atual - ano_nascimento
    #     return cls(nome, idade )

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand