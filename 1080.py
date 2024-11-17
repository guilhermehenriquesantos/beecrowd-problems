valores = []

for i in range (0,100):
    valor = int(input())
    valores.append(valor)

print('{}'.format(max(valores)))

for i in range(0, len(valores)):
    if (max(valores) == valores[i]):
        print(i+1)
        break
