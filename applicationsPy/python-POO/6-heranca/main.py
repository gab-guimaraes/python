import Cliente

c1 = Cliente.Client(23, 'Gabriel')

c2 = Cliente.Student(29, 'Joana')

c3 = Cliente.ClientVip(2, 'Abu')

print(c1.nome)
print(c2.nome)
print(c1.nomeclasse)
print(c2.nomeclasse)
print(c3.coco())

