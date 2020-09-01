from itertools import count, combinations

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

""""
Combinations, Permutations e Product
1-ordem nao importa
2-ordem importa
"""

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia']

for grupo in combinations(pessoas, 2):
    print(grupo)
