
from aula105_classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta Mormaii', 100)
p2 = Produto('iPhone', 100000)
p3 = Produto('Caneca SeuMadruga', 30)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)


carrinho.listar_produtos()

print(carrinho.somar_total())