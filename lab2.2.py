from random import randint as random

def show(x):
    print('\n')
    for i in range(len(x[0])):
        print(x[i])

def task1(long):
    list = [random(-100, 100) for i in range(long)]; print(list)
    list.sort(reverse = True); print(list)
task1(5)

def task2(long):
    n = 0
    list = [[random(-100, 100) for i in range(long)] for i in range(long)]; show(list)
    longList = []
    for i in range(long):
        for j in range(long):
            longList.append(list[i][j])
    print(longList)
    longList.sort(reverse = True)
    for i in range(long):
        for j in range(long):
            list[i][j] = longList[n]
            n += 1
    show(list)

task2(5)