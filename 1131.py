dicionario = {}
contadorPartidas = 0
dicionario['inter'] = []
dicionario['gremio'] = []
empates = 0
quantidadeVitoriasInter = 0
quantidadeVitoriasGremio = 0

while (True):
    inter, gremio = map(int, input().split())

    if (inter > gremio):
        dicionario['inter'].append('Ganhou de {}x{}'.format(inter, gremio))
        dicionario['gremio'].append('Perdeu de {}x{}'.format(inter, gremio))
    elif(inter < gremio):
        dicionario['gremio'].append('Ganhou de {}x{}'.format(inter, gremio))
        dicionario['inter'].append('Perdeu de {}x{}'.format(inter, gremio))
    elif(inter == gremio):
        dicionario['inter'].append('Empate de {}x{}'.format(inter, gremio))
        dicionario['gremio'].append('Empate de {}x{}'.format(inter, gremio))

    contadorPartidas += 1

    novoGrenal = int(input('Novo grenal (1-sim 2-nao)\n'))

    if (novoGrenal == 2):
        break

print('{} grenais'.format(contadorPartidas))

for k,v in dicionario.items():
    
    if (k == 'inter'):
        for resultado in v:
            if ('Ganhou' in resultado):
                quantidadeVitoriasInter += 1
            elif ('Empate' in resultado):
                empates  += 1
        
        print('Inter:{}'.format(quantidadeVitoriasInter))
    
    if (k == 'gremio'):
        for resultado in v:
            if ('Ganhou' in resultado):
                quantidadeVitoriasGremio += 1
        
        print('Gremio:{}'.format(quantidadeVitoriasGremio))

print('Empates:{}'.format(empates))

if (quantidadeVitoriasInter > quantidadeVitoriasGremio):
    print('Inter venceu mais')
elif (quantidadeVitoriasGremio > quantidadeVitoriasInter):
    print('Gremio venceu mais')
elif (quantidadeVitoriasInter == quantidadeVitoriasGremio):
    print('Nao houve vencedor')