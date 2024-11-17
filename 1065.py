a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a,b,c,d,e]
resposta = []

for numero in lista:
    if (numero % 2 == 0):
        resposta.append(numero)

print("{} valores pares".format(len(resposta)))