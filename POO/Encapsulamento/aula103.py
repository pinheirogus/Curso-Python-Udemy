"""
métodos e atributos podem ser públicos, protegidos ou privados

-públicos são aqueles que podem ser acessados dentro e fora da classe.
-protegidos são aqueles que podem ser acessados apenas dentro da classe e de suas filhas
-privados são aqueles que só estão disponíveis dentro daquelas classe. (usar um ou dois underlines)

isso tudo serve pra proteger a sua aplicação

"""

class BaseDeDados:
    def __init__(self):
        # Por convenção, atributos com um underline são privados, não acesse.
        # Atributos com dois underlines são proibidos de serem acessados fora da classe.
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados


base1 = BaseDeDados()
base1.inserir_cliente(1, 'Otávio')
base1.inserir_cliente(2, 'Miranda')
base1.inserir_cliente(3, 'Rose')
#
# base1.apagar_cliente(2)
# base1.listar_clientes()

# Normalmente essa linha quebraria o código, mas o Python renomeia o atributo para evitar isso
base1.__dados = 'Outra coisa'

print(base1.__dados)
print()
print(base1._BaseDeDados__dados)