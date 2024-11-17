N = int(input())
total_coelhos = 0
total_ratos = 0
total_sapos = 0

dicionario = {}

for i in range(0, N):
    Quantia, Tipo = map(str, input().split(' '))

    if (Tipo not in dicionario):
        dicionario[Tipo] = int(Quantia)
    else:
        dicionario[Tipo] = dicionario[Tipo] + int(Quantia)

for k,v in dicionario.items():
    if (k == 'C'):
        total_coelhos = v
    elif (k == 'R'):
        total_ratos = v
    elif (k == 'S'):
        total_sapos = v

print('Total: {} cobaias'.format(sum(dicionario.values())))
print('Total de coelhos: {}'.format(total_coelhos))
print('Total de ratos: {}'.format(total_ratos))
print('Total de sapos: {}'.format(total_sapos))
print('Percentual de coelhos: {:.2f} %'.format((total_coelhos/sum(dicionario.values())*100)))
print('Percentual de ratos: {:.2f} %'.format((total_ratos/sum(dicionario.values())*100)))
print('Percentual de sapos: {:.2f} %'.format((total_sapos/sum(dicionario.values())*100)))