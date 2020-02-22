f = open("assets/lab.txt", "r")
f1 = open("assets/lab2.txt", "a")
strF = str(f.read())
list = []
num = str("")
for i in strF:
    if i != (" "):
        num += i
    elif i == (" "):
        list.append(int(num))
        num = ""
print(list)

for i in range(len(list)):
    if list[i]%2 == 0:
        f1.write(str(list[i]) + str(" "))
f.close()
f1.close()

