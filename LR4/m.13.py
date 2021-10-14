group_17, group_18, group_19 = ["vadim", "nikita"], ["artem", "maxim", "andrey"], ["valera"]
all = [group_17, group_18, group_19]
students = []
min = 999
max = 0
count = len(group_17) + len(group_18) + len(group_19)
groupMin = []
groupMax = []
for i in range(3):
    if min > len(all[i]):
        min = len(all[i])
        groupMin = all[i]

    if max < len(all[i]):
        max = len(all[i])
        groupMax = all[i]

for i in range(3):
    students.extend(all[i])

students.sort()
print("Count:", count, "\nMin:", min, ", group = ", groupMin, "\nMax:", max, ", group = ", groupMax, "\nStudents = ", students)
