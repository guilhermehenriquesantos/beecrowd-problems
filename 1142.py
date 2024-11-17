referencial = 1

N = int(input())

for i in range (0, N):
    resultado = []
    for j in range (referencial, referencial + 3):
        resultado.append(j)
        if (j == referencial + 2):
            resultado.append('PUM')
            referencial = referencial + 4

    print (" ".join(map(str,resultado)))