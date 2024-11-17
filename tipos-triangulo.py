def ordenarLados(A, B, C):
    array = [A, B, C]
    maior_valor = max(array)

    if (maior_valor > A):
        auxiliar = A
        A = maior_valor
        if (maior_valor == B):
            B = auxiliar
        else:
            if (maior_valor == C):
                C = auxiliar

    return A, B, C

if __name__=='__main__':
    A, B, C = map(float, input().split())
    A, B, C = ordenarLados(A, B, C)

    if (A >= (B+C)):
        print('NAO FORMA TRIANGULO')
    elif (A**2 == (B**2 + C**2)):
        print('TRIANGULO RETANGULO')
    elif (A**2 > (B**2 + C**2)):
        print('TRIANGULO OBTUSANGULO')
    elif (A**2 < (B**2 + C**2)):
        print('TRIANGULO ACUTANGULO')

    if (A == B == C):
        print('TRIANGULO EQUILATERO')

    if ((A == B or B == C or A == C) and not (A == B == C)):
        print('TRIANGULO ISOSCELES')
