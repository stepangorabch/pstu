#1. Написать программу вычисления суммы факториалов всех нечетных чисел от 1 до 9.
#2. Дано четное число n > 2. Проверить для него гипотезу Гольдбаха: каждое четное представляется в виде суммы двух простых чисел.

#задача 1
def factorial(x):
    factDef = 1
    for i in range(1,x+1):
        factDef = factDef*i
    return(factDef)

def SuperEpicMegaFunction(k):
    sum = 0
    for j in range(1, k+1):
        if j%2 == 1:
            sum += factorial(j)
            print('Номер фаториала:', j, 'Сумма равна:', sum)
    print('Сумма факториалов равна:', sum)

SuperEpicMegaFunction(int(input('\nВведите число: ')))

#задача 2

