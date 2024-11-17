a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista_entradas = [a,b,c,d,e,f]
lista_saida = []

for numero in lista_entradas:
    if (numero > 0):
        lista_saida.append(numero)

print("{} valores positivos".format(len(lista_saida)))