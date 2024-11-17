X = int(input())
Y = int(input())
soma = 0
menor = X
maior = Y

if (X > Y):
    maior = X
    menor = Y

for i in range(menor, maior + 1):
    if (i % 13 != 0):
        soma = soma + i

print(soma)