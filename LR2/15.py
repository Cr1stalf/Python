t = float(input())
t = t % 60 % 5
if t < 3:
    print('green')
else:
    print('red')