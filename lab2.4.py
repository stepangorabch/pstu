from random import randint as random
numbers = [random(-100, 100) for i in range(int(input("some len: ")))]
print(numbers)

with open("lab.txt", "a") as f:
    for i in range(len(numbers)):
        f.write(str(numbers[i])+str(" "))



