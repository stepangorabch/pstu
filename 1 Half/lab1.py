#1.	Даны три действительных числа. Возвести в квадрат те из них, значения которых неотрицательные, и в четвертую степень – значения которых отрицательные. 
#2.	Дано число   Напечатать в порядке возрастания числа:  ,  ,   Если при каком-либо   некоторые из выражений не имеют смысла, вывести сообщение об этом и сравнивать значения только тех, которые имеют смысл.
#3.	Дано трехзначное число. Выяснить, является ли оно палиндромом.
#4.	Даны числа   Найти значение выражения



from random import randint as random
from random import random as miniRandom
from random import uniform as megaRandom
from math import cos



#задача 1
def task1():
    e = miniRandom()
    n = random(1,20)
    i = 1
    list1 = []
    list2 = []
    print('e =',e, 'n=',n)
    sum = 0
    while i != n:
        a = ((2*i)-1)/(2**i)
        print('i =', i, '    a =',a)
        if  abs(a) >= e:
            sum += abs(a)
            print("\nsum =", sum)
            iStr = ("i = [" + str(i) + "]")
            list1.append(abs(a))
            list2.append(iStr)
            print(list1, '\n')
        i += 1

    print( "\nитог: \nсумма элеметов :", sum, "\nсписок элеменотов:", list1, "\nномера элеменотов:",list2)



#задача 2
def task2():
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum2plus = 0
    sum3plus = 0
    n = random(1,10)
    print("\n\n\nn =", n)

    for i in range(1,n):
        sum1 = sum1 + (i**5)
        sum2 = sum2 + (i**7)
        sum2plus = sum1+sum2
        sum3plus = sum3plus+i
        sum3 = 2*(sum3plus**4)
        print("\n(1 ** 5 + 2**5   ...   n**5) = ", sum1, "      (1 ** 7 + 2**7  ...  n**7) = ", sum2)
        print("sum1 + sum2 = ", sum2plus, "     2*(1 + 2  ... + n)**4 = ", sum3, "\n")



#задача 3
def task3():
    x = megaRandom(-1000,1000)
    n = random(2,100)
    cosinus = cos(x)
    sum1 = cosinus
    print("\n\n\nx = ", x, "\ncos(x) = ", cosinus, "\nn = ", n, "\n\n")
    for i in range(1,n):
        cosinus = cos(cosinus)
        sum1 += cosinus
        print("sum1 = ", sum1, "i = ", i)

task1()
task2()
task3()
