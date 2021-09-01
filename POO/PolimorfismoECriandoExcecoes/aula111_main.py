"""
PolimorfismoECriandoExcecoes é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura)
mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros

Como o exemplo da aula 110 de classes abstratas!
"""

class TaErradoBurroError(Exception):
    pass

def testar():
    raise TaErradoBurroError('Olokomeu')

try:
    testar()
except TaErradoBurroError as error:
    print(f'Erro: {error}')