N = int(input())

if N < 10000:
    dentro = []
    fora = []

    for i in range (0, N):
        valor = int(input())

        if valor in range(10, 20):
            dentro.append(valor)
        else:
            fora.append(valor)

    print("{} in".format(len(dentro)))
    print("{} out".format(len(fora)))