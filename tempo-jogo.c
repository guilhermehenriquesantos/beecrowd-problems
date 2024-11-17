#include <stdio.h>

int main()
{
    int hora_inicial, minuto_inicial, hora_final, minuto_final, tempo, tempo_hora, tempo_minuto;

    scanf("%d %d %d %d", &hora_inicial, &minuto_inicial, &hora_final, &minuto_final);

    tempo = (((hora_final * 60) + minuto_final) - ((hora_inicial * 60) + minuto_inicial));

    if (tempo <= 0)
    {
        tempo = tempo + (24 * 60);
    }

    tempo_hora = tempo / 60;
    tempo_minuto = tempo % 60;

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", tempo_hora, tempo_minuto);

    return 0;
}
