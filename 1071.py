X = int(input())
Y = int(input())
menor = 0
maior = 0
resultado = 0

if (X < Y):
    menor = X
    maior = Y
elif (X > Y):
    menor = Y
    maior = X
else:
    print(X - Y)
    exit()


for i in range (menor+1, maior):
    if (i % 2 != 0):
        resultado = resultado + i

print(resultado)