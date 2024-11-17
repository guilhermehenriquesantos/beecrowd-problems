N = int(input())
lista = []

for i in range(0, N):
    x, y = map(int, input().split())
    resultado = 0

    maior = y
    menor = x

    if (x > y):
        maior = x
        menor = y

    if (x != y):
        for j in range (menor+1, maior):
            if (j % 2 != 0):
                resultado = resultado + j

    lista.append(resultado)

for resultado in lista:
    print(resultado)

