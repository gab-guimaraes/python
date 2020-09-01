file = open('abc.txt', 'w+')
file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')

# return to start of file

file.seek(0, 0)
print('Reading Lines...')
print(file.read())
print('####################')

file.seek(0, 0)

print(file.readline(), end='')
print(file.readline(), end='')

print('#######################')


file.close()
