if __name__=="__main__":
    qtd_segundos = 0
    qtd_minutos = 0
    qtd_horas = 0
    qtd_dias = 0

    data_inicio =  input().split(' ')
    horas_inicio =  input().split(' : ')
    data_fim =  input().split(' ')
    horas_fim =  input().split(' : ')

    hora_inicio = int (horas_inicio[0])
    minuto_inicio = int (horas_inicio[1])
    segundo_inicio = int (horas_inicio[2])
    hora_fim = int (horas_fim[0])
    minuto_fim = int (horas_fim[1])
    segundo_fim = int (horas_fim[2])

    qtd_segundos = segundo_fim - segundo_inicio
    if (qtd_segundos < 0):
        qtd_segundos = 60 + qtd_segundos
        qtd_minutos = qtd_minutos - 1

    qtd_minutos = minuto_fim - minuto_inicio + qtd_minutos
    if (qtd_minutos < 0):
        qtd_minutos = 60 + qtd_minutos
        qtd_horas = qtd_horas - 1

    qtd_horas = hora_fim - hora_inicio + qtd_horas
    if (qtd_horas < 0):
        qtd_horas = 24 + qtd_horas
        qtd_dias = qtd_dias - 1

    qtd_dias = int(data_fim[1]) - int(data_inicio[1]) + qtd_dias

    print("{} dia(s)".format(qtd_dias))
    print("{} hora(s)".format(qtd_horas))
    print("{} minuto(s)".format(qtd_minutos))
    print("{} segundo(s)".format(qtd_segundos))
