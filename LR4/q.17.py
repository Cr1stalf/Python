A = [[1, 10], [2, 20], [3, 30],[4,40]]
new = [ ]
for i in range(len(A)):
    for j in range(len(A[i])):
        new.append(str(A[i][j]))
A = [(','.join(new))]
print(A)