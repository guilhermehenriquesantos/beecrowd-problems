N = int(input())

for i in range(0, N):
    X, Y = map(int, input().split())
    soma = 0

    while (Y > 0):
        if (X % 2 != 0):
            soma = soma + X
            X += 1
            Y -= 1
        else:
            X += 1

    print(soma)
