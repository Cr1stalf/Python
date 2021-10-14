a = [5, 4, 1, 2, 6, 7, 5, 9]
if len(a) % 2 != 0:
    x = a.pop()
    for i in range(1, len(a), 2):
        a[i], a[i - 1] = a[i - 1], a[i]
    a.append(x)
else:
    for i in range(1, len(a), 2):
        a[i], a[i - 1] = a[i - 1], a[i]
print(a)
