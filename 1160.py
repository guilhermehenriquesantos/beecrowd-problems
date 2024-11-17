T = int(input())
resposta = []

if (1 <= T <= 3000):
    for i in range(0, T):
        QtdAnos = 0
        PA, PB, G1, G2 = map(str, input().split())
        
        PA = int(PA)
        PB = int(PB)
        G1 = float('{:.1f}'.format(float(G1)))
        G2 = float('{:.1f}'.format(float(G2)))

        while(PA <= PB):
            PA = PA + int(PA*G1/100)
            PB = PB + int(PB*G2/100)
            QtdAnos += 1

            if (QtdAnos > 100):
                break

        if (QtdAnos > 100):
            resposta.append('Mais de 1 seculo.')
        else:
            resposta.append('{} anos.'.format(QtdAnos))

for anos in resposta:
    print(anos)