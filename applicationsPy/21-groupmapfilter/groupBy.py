alunos = [
    {'nome': 'Gabriel', 'nota': 'A'},
    {'nome': 'Jao', 'nota': 'B'},
    {'nome': 'Edward', 'nota': 'D'},
    {'nome': 'Bella', 'nota': 'C'}
]

alunos.sort(key=lambda item: item['nome'])
print(alunos)

