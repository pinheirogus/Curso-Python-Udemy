# Objetos existem independentes

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f' {produto.nome}, R$ {produto.valor:.2f}')

    def somar_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f' R$ {total:.2f}'


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor