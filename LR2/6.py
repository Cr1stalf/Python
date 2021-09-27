bYears, bMonths, pYears, pMonths = map(int, input().split())

age = pYears-bYears-1

if pMonths == bMonths:
    age += 1

print(age)