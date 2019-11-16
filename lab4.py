#1. Дана последовательность натуральных чисел a1, a2, ..., an. Создать массив из четных чисел этой последовательности. Если таких чисел нет, то вывести сообщение об этом факте.
#2. Дана последовательность целых чисел a1,.a2, ..., an, Указать все пары элементов массива, для которых сумма равна n.
#3. Даны две последовательности a1, a2, ..., an и b1, b2, ..., bm (m < n). В каждой из них члены различны. Верно ли, что все члены второй последовательности входят в первую последовательность?

def superMegaEpicFunctionVolume2(x):
    l = [i for i in range(1,x+1)]
    l2 = []
    print(l)
    for i in range (x):
        if l[i]%2 == 0:
            l2.append(l[i])
            print(l2)

superMegaEpicFunctionVolume2(int(input("введите число:")))



def superMegaEpicFunctionVolume3(x):
    l = [i for i in range(1,x+1)]
    l2 = []
    sumVar = str(" ")
    print(l)
    for i in range (x):
        a = l[i]
        print("a = ", a)
        if a == x/2:
            sumVar = (str(a) + " + " + str(l[i]))
            l2.append(sumVar)
            break   
        for k in range(x):
            #print("     k = ", k)
            if (a + l[k]) == x:
                sumVar = (str(a) + " + " + str(l[k]))
                l2.append(sumVar)    
    print(l2)

superMegaEpicFunctionVolume3(int(input("введите число:")))

