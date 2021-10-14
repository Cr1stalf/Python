a = ["vadim", "vadim", "nikita", "serega", "andrey", "andrey"]
count = 0
for i in range(1, len(a), 2):
    if a[i] == a[i-1]:
        count += 1
print(count)
