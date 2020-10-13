class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for v in self.enderecos:
            print(v.cidade, v.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


cliente1 = Cliente('john', 22)
cliente1.enderecos('LA', 'LA')

cliente2 = Cliente('joao', 12)
cliente2.enderecos('SP', 'SP')