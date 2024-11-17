while(True):
    X = int(input())

    if (X == 0):
        break
    else:
        contador = 0
        soma = 0
        while(True):
            if (X % 2 == 0):
                soma = soma + X
                contador += 1
                X += 2
            else:
                X += 1

            if (contador == 5):
                break

        print(soma)