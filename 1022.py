def encontra_maior_divisor_comum(numerador, denominador):
    if (numerador == denominador):
        return numerador
    else:
        maior = max(numerador, denominador)
        menor = min(numerador, denominador)

        while menor != 0:
            resto = maior % menor
            maior = menor
            menor = resto

        return abs(maior)


if __name__ == '__main__':
    N = int(input())
    resultados = []

    for i in range(0, N):
        N1, divisor, D1, operacao, N2, divisor, D2 = map(str, input().split())

        N1 = int(N1)
        D1 = int(D1)
        N2 = int(N2)
        D2 = int(D2)

        if (operacao == '+'):
            numerador = (N1*D2 + N2*D1)
            denominador = (D1*D2)
            soma = '{}{}{}'.format(numerador, divisor, denominador)
            simplificada = '{}{}{}'.format(int(numerador/encontra_maior_divisor_comum(numerador, denominador)), divisor, int(denominador/encontra_maior_divisor_comum(numerador, denominador)))
            resultados.append('{} = {}'.format(soma, simplificada))
        elif(operacao == '-'):
            numerador = (N1*D2 - N2*D1)
            denominador = (D1*D2)
            soma = '{}{}{}'.format(numerador, divisor, denominador)
            simplificada = '{}{}{}'.format(int(numerador/encontra_maior_divisor_comum(numerador, denominador)), divisor, int(denominador/encontra_maior_divisor_comum(numerador, denominador)))
            resultados.append('{} = {}'.format(soma, simplificada))
        elif(operacao == '*'):
            numerador = (N1*N2)
            denominador = (D1*D2)
            soma = '{}{}{}'.format(numerador, divisor, denominador)
            simplificada = '{}{}{}'.format(int(numerador/encontra_maior_divisor_comum(numerador, denominador)), divisor, int(denominador/encontra_maior_divisor_comum(numerador, denominador)))
            resultados.append('{} = {}'.format(soma, simplificada))
        elif(operacao == '/'):
            numerador = (N1*D2)
            denominador = (N2*D1)
            soma = '{}{}{}'.format(numerador, divisor, denominador)
            simplificada = '{}{}{}'.format(int(numerador/encontra_maior_divisor_comum(numerador, denominador)), divisor, int(denominador/encontra_maior_divisor_comum(numerador, denominador)))
            resultados.append('{} = {}'.format(soma, simplificada))

    for resultado in resultados:
        print(resultado)
