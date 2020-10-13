import random
import time
from concurrent.futures import thread
from threading import Thread

from playsound import playsound

print('Bem vindo ao chapéu seletor...')

time.sleep(3)

name = input('Qual o seu nome?')

print('Bem vindo ', name)

randomNumber = random.randint(0, 3)


def tocar_corvinal():
    playsound('corvinal.aif')


def tocar_sonserina():
    playsound('sonserina.aif')


def tocar_grifnoria():
    playsound('grifnoria.aif')


def tocar_lufa():
     playsound('lufa_lufa.aif')


"""
t3 = Thread(target=vai_demorar, args=('ola', 10))
t3.start()
"""


if randomNumber == 0:
    print('A sua casa é')
    time.sleep(2)
    print('**** GRIFINORIA *********')
    t1 = Thread(target=tocar_grifnoria())
    t1.start()

if randomNumber == 1:
    print('A sua casa é')
    time.sleep(2)
    print('**** SONSERINA *********')
    t1 = Thread(target=tocar_sonserina())
    t1.start()

if randomNumber == 2:
    print('A sua casa é')
    time.sleep(2)
    print('**** LUFALUFA *********')
    t1 = Thread(target=tocar_lufa())
    t1.start()

if randomNumber == 3:
    print('A sua casa é')
    time.sleep(2)
    print('**** CORVINAL *********')
    t1 = Thread(target=tocar_corvinal())
    t1.start()



