class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for v in self.produtos:
            print(v.nome, v.valor)

    def soma_total(self):
        total = 0
        for v in self.produtos:
            total += v.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
