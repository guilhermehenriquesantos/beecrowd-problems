a = int(input())
e = int(input())
i = int(input())
o = int(input())
u = int(input())

lista = [a,e,i,o,u]
pares = []
impares = []
positivos = []
negativos = []


for numeral in lista:
    if (numeral % 2 == 0):
        pares.append(numeral)
    else:
        impares.append(numeral)

    if (numeral < 0):
        negativos.append(numeral)
    elif (numeral > 0):
        positivos.append(numeral)

print('{} valor(es) par(es)'.format(len(pares)))
print('{} valor(es) impar(es)'.format(len(impares)))
print('{} valor(es) positivo(s)'.format(len(positivos)))
print('{} valor(es) negativo(s)'.format(len(negativos)))