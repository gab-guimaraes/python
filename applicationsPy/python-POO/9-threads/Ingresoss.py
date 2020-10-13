from threading import Thread, Lock


class Ingresos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() #trancando

        if self.estoque < quantidade:
            print('nao temos ingressos suficiente')
            self.lock.release()
            return
        self.estoque -= quantidade
        print('voce comprou', quantidade, 'ingresoss. ainda temos', self.estoque)

        self.lock.release() #abrindo


ingressos = Ingresos(10)

for i in range(1, 20):
    t = Thread(target=ingressos.comprar, args=(i,))
    t.start()

