N = int(input())
lista = []

for i in range (0, N):
    a, b, c = map(float, input().split(' '))

    media_ponderada = ((a*2) + (b*3) + (c*5))/(2+3+5)

    lista.append(media_ponderada)

for resultado in lista:
    print('{:.1f}'.format(resultado))