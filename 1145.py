X, Y = map(int, input().split())
contador = 0
resultado = []

if ((1 < X < 20) and (X < Y < 100000)):
    for i in range (1, Y+1):
        resultado.append(i)
        contador += 1

        if (contador == X):
            contador = 0
            print(" ".join(map(str, resultado)))
            resultado = []