x = int(input())
y = x
min = 999
count = 0
for i in range(1, len(str(x)) + 1):
    if min > (x % 10):
        min = x % 10
    x //= 10

while y > 0:
    if(y % 10 == min):
        count += 1
    y //= 10
print(count)
