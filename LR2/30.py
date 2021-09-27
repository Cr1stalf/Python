h, m, s = map(int, input().split())
print(round(h*(360/12) + m*(360/12/60) + s*(360/12/60/60)), 'градусов')