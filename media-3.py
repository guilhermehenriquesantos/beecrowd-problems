N1, N2, N3, N4 = map (float, input().split())


media = (N1*2 + N2*3 + N3*4 + N4*1)/(2+3+4+1)

print('Media: {:.1f}'.format(media))

if (media >= 7.0):
    print('Aluno aprovado.')
elif(media < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    NE = float(input())
    print('Nota do exame: {}'.format(NE))
    media_final = (media + NE) / 2
    if (media_final >= 5.0):
        print('Aluno aprovado.')
    elif(media_final <= 4.9):
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media_final))