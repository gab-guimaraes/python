class Pessoa:

    # Init é o método construtor em Python
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        print(self.nome, 'está comendo')
        self.comendo = True

        #@classmethod

    @staticmethod
    def imprime_status():
        print('print status')



