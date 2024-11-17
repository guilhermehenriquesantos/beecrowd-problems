hora_inicial, hora_termino = map(int, input().split())

try:
    tempo = 0
    if (hora_inicial >= 0 and hora_inicial <= 23 and hora_termino >= 0 and hora_termino <= 23):
        if (hora_inicial > hora_termino):
            tempo = 24 - hora_inicial + hora_termino
        elif (hora_inicial < hora_termino):
            tempo = hora_termino - hora_inicial
        elif (hora_inicial == hora_termino):
            tempo = 24

        print('O JOGO DUROU {} HORA(S)'.format(tempo))
except:
    pass