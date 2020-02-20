import random
def shellSort(alist):
    shag = len(alist)//2
    while shag > 0:
      for startposition in range(shag):
        gapInsertionSort(alist,startposition,shag)
      #print("шаг",shag,"\nсписок",alist)
      shag = shag // 2
    return(alist)

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        element = alist[i]
        position = i
        while position>=gap and alist[position-gap]>element:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=element

alist = random.sample(range(10),9)
print("задание первое\nдан массив:",alist)
shellSort(alist)
print("ответ:",alist)

def second(x):
    matrixList = [[random.randint(-10,10) for i in range(x)] for i in range(x)]
    for i in range(x):
         print(matrixList[i])
    print("\n")
    for i in range(x):
         matrixList[i] = shellSort(matrixList[i])
         print(matrixList[i])

second(int(input("введите размер матрицы ")))
