x = int(input())
if x//10 > x % 10:
    print('Первая')
elif x % 10 > x//10:
    print('Вторая')
else:
    print('Цифры одинаковы')