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
    for i in range(len(matrixList[0])):
        print(matrixList[i])


for i in range(1, 9):
    matrix4(i)