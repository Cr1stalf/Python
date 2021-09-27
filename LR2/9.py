a, b = map(int, input().split())
if b % a == 0:
    print('Число ', a, ' является делителем числа ', b)
else:
    print('Число ', a, ' не является делителем числа ', b)