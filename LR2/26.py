for i in range(1, 1000):
    if (str(i % 10) + str((i - i % 10) // 10)) == '237':
        print(i)
        