from random import randint as random
#xfile = open("lab.txt", 'a')
#x = int(input("some len: "))
numbers = [random(-100,100) for i in range(int(input("some len: ")))]
print(numbers)
with open("lab.txt",'w',encoding = 'utf-8') as f:
    print(numbers, file = f)
    f.close()
files = open("lab.txt", 'r', encoding = 'utf-8')
files.read()


