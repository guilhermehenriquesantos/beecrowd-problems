N = int(input())

if (1 < N < 1000):
    for i in range(1, N+1):
        quadrado = i ** 2
        cubo = i ** 3
        print ('{} {} {}'.format(i, quadrado, cubo))
        print ('{} {} {}'.format(i, quadrado+1, cubo+1))