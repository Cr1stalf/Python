from random import randrange

def evenElements (a:list):
    print('Even elements:')
    for i in range(20):
        if a[i] % 2 == 0:
            print(a[i], end=' ')

def elementsEndsZero (a:list):
    print('Zero terminated elements:')
    for i in range(20):
        if a[i] % 10 == 0:
            print(a[i], end=' ')

a = [randrange(1,1000) for i in range(20)]

print('Array:\n', a)

evenElements(a)
print('\n')
elementsEndsZero(a)