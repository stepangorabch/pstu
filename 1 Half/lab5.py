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
        id = str("Строка: ") + str(i+1) + str(" Столбец: ") + str(m)
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

#matrix2(int(input("\nВведите число: ")))

def matrix3(x, y):
    D = [random(1,2) for i in range(y)]
    A = [[random(1,2) for j in range(y)] for i in range(x)]
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
                n = i

        if len(checkList) == len(D):
            numList.append(n+1)
                #print('\n', checkList)
            
    if len(numList) == 0:
        print("Одинаковых строк нет!")
    else:
        print('\n',numList)

#matrix3(int(input("\nВведите число строк: ")),int(input("Введите число столбцов: ")))


def matrix4(x):
    matrixList = []
    for i in range(x):
        matrixList.append([0] * x)
    
    matrixList[0][0] = 1
    #print(matrixList)
    
    idX = 0; idY = 0
    n = 1; num = x-2

    for i in range((2*x)-1):
        #print("\ni = ",i)
        if idX == 0 and i < x-1:
            #print("X")
            #print("idY :", idY, "idX: ", idX)
            idY += 1
            n += 1
            matrixList[idY][idX] = n
            for k in range(i+1):
                n += 1
                idY -= 1
                idX += 1
                matrixList[idY][idX] = n
        
        elif idY == 0 and i < x-1:
            #print("\nY")
            #print("idY :", idY, "idX: ", idX)
            idX += 1
            n += 1
            matrixList[idY][idX] = n
            for k in range(i+1):
                n += 1
                idX -= 1
                idY += 1
                matrixList[idY][idX] = n

        elif idX == (x-1) and i >= x:
            #rint("\nX")
            #print("idY :", idY, "idX: ", idX)
            idY += 1
            n += 1
            matrixList[idY][idX] = n
            for k in range(num):
                n += 1
                idX -= 1
                idY += 1
                matrixList[idY][idX] = n
            num -= 1

        elif idY == (x-1) and i >= x:
            #print("\nY")
            #print("idY :", idY, "idX: ", idX)
            idX += 1
            n += 1
            matrixList[idY][idX] = n
            for k in range(num):
                n += 1
                idY -= 1
                idX += 1
                matrixList[idY][idX] = n
            num -= 1

    print("\n")
    for i in range(x):
        matrixList[i].reverse()
    for i in range(len(matrixList[0])):
        print(matrixList[i])

matrix4(int(input("\nВведите размер матрицы: ")))