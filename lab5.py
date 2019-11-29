from random import randint as random

def matrix(x, y):
    megaList = [[random(1,99) for j in range (y)] for i in range(x)]
    minimumList = []
    n = 0
    m = 0
    for i in range(x):
        print(megaList[i])

    for i in range(x):
        n = megaList[i][0]
        for j in range(y-1):
            if megaList[i][j+1] < n:
                n = megaList[i][j+1]
                m = j+2
                
        minimumList.append(n)
        print("\nСтрока: ", i+1, "Столбец: ", m)
        print(minimumList)
    
    n = minimumList[0]
    for k in range(len(minimumList)):
        if minimumList[k] > n:
            n = minimumList[k]
    print("\nМаксимальный элемент из минимальных: ", n)

matrix(int(input("Введите число строк: ")),int(input("Введите число столбцов: ")))

def matrix2(x):
    matrixList = [[] * x for i in range(x)]
    n = 1
    for i in range(x):
        for j in range(x):
            matrixList[i].append(n)
            n += 1
    for i in range(x):
        print(matrixList[i])

#matrix2(int(input("Введите число: ")))

def matrix3(x, y):
    D = [random(1,6) for i in range(y)]
    A = [[random(1,3) for j in range(y)] for i in range(x)]
    numList = []
    print(D)
    print("\n")
    for i in range(x):
        print(A[i])
    
    for i in range(x):
        checkList = []
        for j in range(y):
            n = 0
            if A[i][j] == D[j]:
                checkList.append(A[i][j])
                n = j

        if len(checkList) == len(D):
            numList.append(n)
            #print('\n', checkList)
            
    if len(numList) == 0:
        print("Одинаковых строк нет!")
    else:
        print('\n',numList)

matrix3(int(input("Введите число строк: ")),int(input("Введите число столбцов: ")))
    

