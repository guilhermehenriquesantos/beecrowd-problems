a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
soma = 0

lista_entradas = [a,b,c,d,e,f]
lista_saida = []

for numero in lista_entradas:
    if (numero > 0):
        lista_saida.append(numero)

for positivo in lista_saida:
    soma = soma + positivo

media_aritmetica = soma / len(lista_saida)

print("{} valores positivos".format(len(lista_saida)))
print("{:.1f}".format(media_aritmetica))