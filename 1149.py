leitura = input().split()

A = int(leitura[0])
N = 0

for valores in leitura:
    if (int(valores) > N and valores != leitura[0]):
        N = int(valores)
        break

soma = 0

for i in range(N):
    soma = soma + A + i

print(soma)