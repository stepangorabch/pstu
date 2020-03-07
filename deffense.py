def show(x):
    max_len = max([len(str(e)) for r in x for e in r])
    for row in x:
        print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))

def show_reverse(x):
    print("\nMATRIX.REVERSE()")
    for i in range(len(x[0])):
        x[i].reverse()
    show(x)

def matrix(n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    show(matrix)

    idX = 0; idY = 0; k = n
    j = 1; a = 1

    for l in range(n):
        if j == 1:
            for i in range(k):
                matrix[idY][idX] = a
                idY += 1; a += 1; 
                print("\n")
                show(matrix)
            k -= 1; j = 2
            idX += 1; idY -= 1

        if j == 2:
            for i in range(k):
                matrix[idY][idX] = a
                idX += 1; a += 1
                print("\n")
                show(matrix)
            idX -= k; idY -= k; j = 1
    
    print("\n")
    show(matrix)

def matrix2(n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    show(matrix)

    idX = n-1; idY = n-1; k = n
    j = 1; a = 1

    for l in range(n):
        if j == 1:
            for i in range(k):
                matrix[idY][idX] = a
                idY -= 1; a += 1; 
                print("\n")
                show(matrix)
            k -= 1; j = 2
            idX -= 1; idY += 1

        if j == 2:
            for i in range(k):
                matrix[idY][idX] = a
                idX -= 1; a += 1
                print("\n")
                show(matrix)
            idX += k; idY += k; j = 1
    
    print("\n")
    show(matrix)

matrix2(5)