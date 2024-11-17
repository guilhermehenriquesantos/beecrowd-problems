notas = []
X = 0

while (X != 2):
    nota = float(input())
    if (nota >= 0 and nota <= 10):
        notas.append(nota)
    else:
        print("nota invalida")

    if (len(notas) == 2):
        media = (notas[0] + notas[1])/2
        print('media = {:.2f}'.format(media))

        notas = []

        X = int(input('novo calculo (1-sim 2-nao)\n'))

        while(X != 1 and X != 2):
            X = int(input('novo calculo (1-sim 2-nao)\n'))