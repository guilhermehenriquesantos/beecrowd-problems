N = int(input())

if (2 < N < 1000):
    for i in range(1, 11):
        print('{} x {} = {}'.format(i, N, N*i))