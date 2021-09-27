n = int(input())
max = 0
min = 10
for i in range(1, len(str(n))+1):
    a = n % 10
    if max < a:
        max = a
        maxPos = i
    if min > a:
        min = a
        minPos = i
    n //= 10
if maxPos > minPos:
    print('Максимальное левее')
else:
    print('Минимальное левее')