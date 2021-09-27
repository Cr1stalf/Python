for a in range(1,100):
    for b in range(1, 100):
        for c in range(1, 100):
            if 10 * a + 5 * b + 0.5 * c == 100 and a + b + c == 100:
                print(a,b,c)