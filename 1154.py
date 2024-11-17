idades = []
while(True):
    idade = int(input())
    if (idade < 0):
        break
    else:
        idades.append(idade)

resultado = sum(idades)/len(idades)

print('{:.2f}'.format(resultado))