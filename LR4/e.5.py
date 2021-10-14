from random import randrange
s = 0
a = [randrange(10, 30) for i in range(42)]
for i in range(42):
    s += a[i]
print(s)