N = int(input())

for i in range(N):
    X, Y = map (int, input().split())

    if (Y != 0):
        resultado = X / Y
        print('{:.1f}'.format(resultado))
    else:
        print('divisao impossivel')