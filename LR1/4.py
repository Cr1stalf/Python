m = int(input())
h = m // 60

while h >=24:
    if h >=24:
        h-=24

print(h, ' часа(ов)', m % 60, ' минут')