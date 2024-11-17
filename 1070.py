X = int(input())
lista = []
contador = 0

if (X % 2 != 0):
    lista.append(X)

while (len(lista) < 6):
    X += 1
    if (X % 2 != 0):
        lista.append(X)

for resultado in lista:
    print(resultado)