y = int(input())
m = y % (360/12) // (360/12/60)
print(round(y // (360/12)), round(m), round(m*(360/12/60)))