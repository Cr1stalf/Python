a = [4, 6, 1, 2, 3, 4, 6, 7, 11, 23, 67]
S = []
count = 0
for i in a:
    if i not in S:
        count +=1
        S.append(i)
print(len(S))