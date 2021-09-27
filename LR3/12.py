n = int(input())

for i in range(1, 100):
    a = 1
    for j in range(2, i+1):
        a*=j

    if a == n:
        print(i)