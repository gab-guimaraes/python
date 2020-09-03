from Pessoa import Pessoa

p1 = Pessoa('Leo', 23)
p2 = Pessoa('Jhon', 11)

print(p1.comendo)
p1.comer()
print(p1.comendo)
print(Pessoa.imprime_status())