n = int(input())
k = int(input())
a = 1
s = 0
for i in range(n, k+1):
    a *= i
    s+=a
print(s)