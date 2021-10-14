A = [9, 8, 6, 5, 7, 4, 3, 2, 1]
t1 = []
t2 = []
print("List:", A)
a1, a2 = map(int, input("Print a1 and a2: ").split())
for i in range(len(A), a2, -1):
    t1.append(A.pop())
t1.reverse()
for i in range(0, a1):
    t2.append(A.pop(0))
t1.extend(A)
t1.extend(t2)
print(t1)