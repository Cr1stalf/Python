a1 = a2 = 1
n = int(input())
for i in range(1, n):
    a = a1+a2
    a1=a2
    a2=a

print(a)
