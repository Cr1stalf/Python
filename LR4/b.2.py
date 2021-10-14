a1, p = map(int, input().split())
A = [a1 + p * (i - 1) for i in range(1, 11)]
print(A)