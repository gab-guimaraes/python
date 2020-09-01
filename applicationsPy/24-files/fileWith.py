with open('creatingFile.txt', 'w+') as file:
    file.write('Line1')
    file.seek(0)
    print(file.readline())

#a - append mode

with open('creatingFile.txt', 'a+') as file:
    file.write('Outra linha')
    file.seek(0)
    print(file.read())

