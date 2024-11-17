X, Y = map(int, input().split())
resultado = []

while (X != Y):
    if (Y > X):
        resultado.append('Crescente')
    elif (X > Y):
        resultado.append('Decrescente')

    X, Y = map(int, input().split())

for resposta in resultado:
    print(resposta)
