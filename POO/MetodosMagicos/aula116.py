class A:
    def __new__(cls, *args, **kwargs):

        # a lógica abaixo permite que você restrinja a apenas uma instância da classe no programa.
        # qualquer instância criada posteriormente será apenas uma cópia da primeira
        if not hasattr(cls, '_objetoJaExiste'):
            cls._objetoJaExiste = object.__new__(cls)

        return cls._objetoJaExiste

    def __init__(self):
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        # Este método permite a chamada da classe como uma função. Exemplo na linha 32
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

a = A()
b = A()
c = A()

print(a == b)
print(b == c)
print(a == c)

print(id(a), id(b), id(c))

print(a(1, 2, 3, 4, 5, nome='Luiz'))
