# we've keys and value
# in list, python create the index for us
# in dictionary, keys are unique, we cannot duplicate it

d1 = {'car': 'mitsubishi', 'brand': ''}
d1['nova chave'] = 'new value'
print(d1)
print(d1['nova chave'])

d2 = dict(chave1='valor da chave')

print(d2)

print('*****************')

d3 = {1: 'key', 1: 'key2', 1: 'key3'}
# key3 is the last value
print(d3)

# check if key exist
if 1 in d3:
    print('exist 1')

