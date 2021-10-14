marks = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
count = 0
average = 0
for i in range(0, len(marks) - 1):
    count+=1
    average+=marks[i]
    print(str(marks[i]) + ";", end="")
average+=marks[len(marks) - 1]
count+=1
average /= count
print(marks[len(marks) - 1], "\nAverage = ", average)
