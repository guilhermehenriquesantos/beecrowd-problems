M, N = map(int, input().split())
contador = 1
dicionario = {}

while (M > 0 and N > 0):
    dicionario[contador] = []

    if (M > N):
        maior = M
        menor = N
    else:
        menor = M
        maior = N

    if (M != N):
        for i in range(menor, maior+1):
            dicionario[contador].append(i)
    else:
        dicionario[contador].append(0)

    contador += 1

    M, N = map(int, input().split())

for valor in dicionario.values():
    print('{} Sum={}'.format(' '.join(map(str, valor)), sum(valor)))
