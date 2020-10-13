from time import sleep
from threading import Thread

""""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t = MeuThread('Thread 1', 5)
t.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

for i in range(5):
    print(i)
    sleep(i)
"""

print('Hello')


# VAI DORMIR PELO TEMPO QUE PASSAR


"""

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t3 = Thread(target=vai_demorar, args=('ola', 5))
t3.start()

t4 = Thread(target=vai_demorar, args=('ola 2', 2))
t4.start()

t5 = Thread(target=vai_demorar, args=('ola 3', 2))
t5.start()

for i in range(10):
    print(i)
    sleep(.5)

"""

# enquanto for viva, loga waiting


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t3 = Thread(target=vai_demorar, args=('ola', 10))
t3.start()

while t3.is_alive():
    print('Waiting...')
    sleep(2)

print('Thread acabou!')

