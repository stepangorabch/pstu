f1 = open('text.txt')
f2 = open('file.txt', 'w')
symbol = str(input("symbol: "))
string = f1.readlines()

for i in range(len(string)):
    if string[i][0] == symbol:
        print(string[i])
        f2.write(string[i])
f1.close()
f2.close()