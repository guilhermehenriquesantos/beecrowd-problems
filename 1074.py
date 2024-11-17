def verificar_tendencia(numero):
    resultado = 'NULL'
    if (numero < 0):
        resultado = 'NEGATIVE'
    elif (numero > 0):
        resultado = 'POSITIVE'

    return resultado


N = int(input())
resultado = []

if (N < 10000):
    for i in range (0, N):
        valor = int(input())

        if (valor == 0):
            resultado.append('NULL')
        elif (valor % 2 == 0):
            tendencia = verificar_tendencia(valor)
            resultado.append('EVEN {}'.format(tendencia))
        elif (valor % 2 != 0):
            tendencia = verificar_tendencia(valor)
            resultado.append('ODD {}'.format(tendencia))

    for valor in resultado:
        print(valor)
