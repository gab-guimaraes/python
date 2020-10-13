from recomendacao import avaliacoes
from math import sqrt

print(pow(5, 2))

''' 
Distancia Euclidiana
Ana vs Claudia
x1 = 3.0, 3.5
y1 = 3.0, 4.0
'''

print(sqrt(pow(3 - 3, 2)))
print(sqrt(pow(3.5 - 4.0, 2)))


def euclidiana(usuario1, usuario2):
    si = {}
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]: si[item] = 1

        if len(si) == 0:
            return 0

        soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
                    for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])
        return 1 / (1 + sqrt(soma))


print(euclidiana('Leonardo', 'Ana'))
