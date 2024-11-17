X = int(input())
Z = int(input())
contador = 0
soma = 0

while (Z <= X):
    Z = int(input())

for i in range(X, Z):
    contador += 1
    soma += i

    if (soma > Z):
        break

print(contador)