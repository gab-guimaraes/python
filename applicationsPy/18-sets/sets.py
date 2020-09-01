# we cannot duplicate values in sets

s1 = {1, 2, 3, 4, 56}

s2 = set()
s2.add(2)
s2.add(5)
s2.add(5)

s2.discard(5)

print(s1)
print(s2)

x3 = {9, 8, 7, 6, 4, 999}
x4 = {9, 4, 5, 67, 42}
# union |
#intersection & - all elements in both sets
#difference - elements only right set
#symmetric_difference - elements in two sets, but not both.

x5 = x3 | x4
x6 = x3 & x4
print(x5)
print(x6)
