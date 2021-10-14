from random import randrange
A = [randrange(30, 45) for i in range(10)]
T = []
for i in range(0, len(A)):
    if A[i] not in T:
        T.append(A[i])
print(T)