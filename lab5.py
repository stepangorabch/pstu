from random import randint as random

def matrix(x, y):
    megaList = [[random(1,99) for j in range (y)] for i in range(x)]
    minimumList = []
    idList = []
    n = 0; m = 0
    z = 0; w = 0
    for i in range(x):
        print(megaList[i])

    for i in range(x):
        n = megaList[i][0]
        for j in range(y-1):
            if megaList[i][j+1] < n:
                n = megaList[i][j+1]
                m = j+1
        print("\nСтрока: ", i+1, "Столбец: ", m+1)
        minimumList.append(n)
        id = str("Строка: ") + str(i+1) + str(" Столбец: ") + str(m+1)
        idList.append(id)
        print(minimumList)
    
    w = minimumList[0]
    for k in range(len(minimumList)):
        if minimumList[k] > w:
            w = minimumList[k]
            z = k

    print("\nМаксимальный элемент из минимальных: ", w)
    print("Номер элемента: ", idList[z])

#matrix(int(input("Введите число строк: ")),int(input("Введите число столбцов: ")))

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

#matrix3(int(input("Введите число строк: ")),int(input("Введите число столбцов: ")))
    

def matrix4(x):
    matrixList = [[] * x for i in range(x)]
    iX = 0; iY = 0; n = 1; num = 1

    while n != x:
        if n%2 == 0:
            iX = 0
            iY = 0
            while iX != 0:
                matrixList[iX][iY] = num
                num += 1
                iX += 1
                if iY != 0:
                    iY -= 1

        else:
            iX = 0
            iY = 0
            while iY != 0:
                matrixList[(iY-1)][iX] = num
                num += 1
                if iX != 0:
                    iX -= 1
                iY += 1

        n += 1

    print(matrixList)

matrix4(5)