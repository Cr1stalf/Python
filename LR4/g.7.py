from random import randrange
points = 120
math = [randrange(1, 101) for i in range(10)]
rus = [randrange(1, 101) for i in range(10)]
inf = [randrange(1, 101) for i in range(10)]
students = ["vadim", "aleksey", "nikita", "ilya", "sergey", "arseniy", "aleksandr", "vlad", "maxim", "borya"]
for i in range(len(students)):
    if math[i] + rus[i] + inf[i] >= points:
        print(i, ":", students[i])