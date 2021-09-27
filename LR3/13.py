n = int(input())
for i in 64, 32, 16, 8, 4, 2, 1:
    a = n // i
    print(a, ' купюр(а) по ', i)
    n %= i
    a = 0
