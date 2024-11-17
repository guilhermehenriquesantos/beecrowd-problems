#include <stdio.h>

int main()
{
    float salario_atual, salario_reajustado, percentual_reajuste;

    scanf("%f", &salario_atual);

    if (salario_atual >= 0 && salario_atual <= 400.00)
    {
        percentual_reajuste = 0.15;
        salario_reajustado = salario_atual + (salario_atual * percentual_reajuste);
    }
    else if (salario_atual >= 400.01 && salario_atual <= 800.00)
    {
        percentual_reajuste = 0.12;
        salario_reajustado = salario_atual + (salario_atual * percentual_reajuste);
    }
    else if (salario_atual >= 800.01 && salario_atual <= 1200.00)
    {
        percentual_reajuste = 0.10;
        salario_reajustado = salario_atual + (salario_atual * percentual_reajuste);
    }
    else if (salario_atual >= 1200.01 && salario_atual <= 2000.00)
    {
        percentual_reajuste = 0.07;
        salario_reajustado = salario_atual + (salario_atual * percentual_reajuste);
    }
    else if (salario_atual > 2000.00)
    {
        percentual_reajuste = 0.04;
        salario_reajustado = salario_atual + (salario_atual * percentual_reajuste);
    }

    printf("Novo salario: %.2f\n", salario_reajustado);
    printf("Reajuste ganho: %.2f\n", salario_reajustado - salario_atual);
    printf("Em percentual: %.0f %%\n", percentual_reajuste*100);

    return 0;
}
