import sys
import time

#lazy evaluation

myList = ['audi', 'mitsubishi', 'subaru']
myBigList = list(range(1000))

for v in myList:
    print(v)

print(sys.getsizeof(myList))
print(sys.getsizeof(myBigList))

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
        return r

g = gera()

for v in g:
    print(v)
