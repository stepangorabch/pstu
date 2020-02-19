#1. Написать программу вычисления суммы факториалов всех нечетных чисел от 1 до 9.
#2. Дано четное число n > 2. Проверить для него гипотезу Гольдбаха: каждое четное представляется в виде суммы двух простых чисел.

#задача 1
def factorial(x):
    factDef = 1
    for i in range(1,x+1):
        factDef = factDef*i
    return(factDef)

def sumFactorial(k):
    sum = 0
    for j in range(1, k+1):
        if j%2 == 1:
            sum += factorial(j)
            print('Номер фаториала:', j, 'Сумма равна:', sum)
    print('Сумма факториалов равна:', sum)
#sumFactorial(int(input('\nВведите число: ')))

#задача 2
def easyNumber(x):
    test = 0
    j = 0
    sqrtX = int(x**0.5)
    print(x**0.5, sqrtX)
    for i in range(1, sqrtX + 1):
        print('i = ', i)
        if (x)%i == 0:
            j += 1
            print("j = ",j)
            
    if j == 1 or x == 2:
        print("число простое")
        test = 1
        return(test)

    else:
        print("число не простое")
        return(test)

def easySum(n):
    if n%2 == 0:
        a = n
        b = 0
        for i in range(1, n):
            a -= 1
            b += 1
            print(a, b)
            if easyNumber(a) == 1:
                print(a, " + ", b)
                break
                
    elif n == 2:
        print("1 + 1")

n = 1
while True:
    if n != 0:
        easySum(n)
        n += 1