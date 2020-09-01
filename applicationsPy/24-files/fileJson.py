import json

d1 = {
    'Pessoa 1': {
        'nome': 'luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 23,
    },
}

print(d1)

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('myFile.json', 'w+') as file:
    file.write(d1_json)

