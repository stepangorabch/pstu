#1.	Даны две точки   и  . Составить алгоритм, определяющий, которая из точек находится ближе к началу координат.
#2.	Заданы размеры A, B прямоугольного отверстия и размеры X, Y, Z кирпича. Определить, пройдет ли кирпич через отверстие.
#3.	Дано двухзначное число. Выяснить:
#   а) является ли сумма его цифр двухзначным числом;
#   б) больше ли сумма его цифр заданного числа А.
#4. Определить, является ли заданное шестизначное число счастливым. (Счастливым называется такое шестизначное число, у которого сумма трех первых цифр равна сумме трех последних.)



from random import randint as random #импорт функции генерации случайных чисел



#задача 1
def task1():
    randomNumber = random(100,999)
    print(randomNumber)
    randomNumber = str(randomNumber)
    a = int(randomNumber[0])
    b = int(randomNumber[1])
    c = int(randomNumber[2])
    print(a, b ,c)
    if (a+b+c)%2 == 0:
        print("Сумма цифр числа", randomNumber, "является четным числом")
    else:
        print("Сумма цифр числа", randomNumber, "не является четным числом")




#задача 2
def task2():
    floor = random(10,99); print("количество этажей:", floor); print("количество квартир:", floor*3)
    flat = random(1, floor*3); print("номер случайной квартиры:", flat)
    flatOnFloor = flat//3; print("номер этажа квартиры:", flatOnFloor)
    if flatOnFloor%2==1:
        print("лифт поднимется  на этаж", flatOnFloor)
    else:
        print("лифт поднимется на этаж", flatOnFloor+1)

task1()
task2()