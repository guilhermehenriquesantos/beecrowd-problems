def modular(valor1, valor2):
    modulo = valor1 - valor2

    if (modulo < 0):
        modulo *= -1

    return modulo


def verifica_triangulo(A, B, C):
    if ((modular(B, C) < A < (B + C)) and (modular(A, C) < B < (A + C)) and (modular(A, B) < C < (A + B))):
        return True
    else:
        return False


A, B, C = map(float, input().split())

if (verifica_triangulo(A, B, C)):
    perimetro_triangulo = A + B + C
    print('Perimetro = {:.1f}'.format(perimetro_triangulo))
else:
    area_trapezio = ((A + B)*C)/2
    print('Area = {:.1f}'.format(area_trapezio))
