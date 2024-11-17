while(True):
    X = int(input())

    if (X == 0):
        break

    resultado = []

    for i in range(1, X+1):
        resultado.append(i)

    print(' '.join(map(str, resultado)))