A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 0
sign = 1
for i in range(0, 9):
    s += sign * A[i]
    sign = -sign
print(s)