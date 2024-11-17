A = 1
B = 1

resultado = A/B

while (True):
    A += 2
    B *= 2

    resultado = resultado + A/B

    if (A == 39):
        break

print('{:.2f}'.format(resultado))