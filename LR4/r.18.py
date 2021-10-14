A = [i for i in range(1, 21)]
for i in range(0, 20):
    if A[i] % 2 == 0:
        A[i] = A[i] * A[i]
    else:
        A[i]+=2
print(A)


