#include <stdio.h>

int calcular_mdc(int maior_numero, int menor_numero)
{
    int mdc, resto_divisao;
    resto_divisao = maior_numero % menor_numero;

    if (resto_divisao == 0)
    {
        mdc = menor_numero;
    }
    else
    {
        mdc = calcular_mdc(menor_numero, resto_divisao);
    }

    return mdc;
}

int main()
{
    // casos de uso, número de figurinhas do portador de figurinhas 1 e número de figurinhas do portador de figurinhas 2
    int N, F1, F2, resultado;

    scanf("%d", &N);

    while (N > 0)
    {
        scanf("%d %d", &F1, &F2);
        if (F2 > F1)
        {
            resultado = calcular_mdc(F2, F1);
        }
        else
        {
            resultado = calcular_mdc(F1, F2);
        }

        printf("%d\n", resultado);

        N--;
    }

    return 0;
}
